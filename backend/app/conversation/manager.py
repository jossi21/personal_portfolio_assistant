from app.models.chat import ChatResponse
from app.models.channel import ChannelMessage
from app.routes.intent_router import IntentRouter
from app.models.agent import AgentType
from app.services.language_service import translate_response
from app.models.language import Language
from app.conversation.state_manager import StateManager
from app.core.container import state_manager

# Agents
from app.agents.welcome_agent import WelcomeAgent
from app.agents.rag_agent import RAGAgent
from app.agents.greeting_agent import GreetingAgent
from app.agents.contact_agent import ContactAgent
from app.agents.language_agent import LanguageAgent
from app.agents.portfolio_agent import PortfolioAgent

# state manager which create conversation state

"""
    Coordinates the conversation flow.

    Responsibilities:
    - Receive user requests
    - Determine user intent
    - Dispatch request to the correct agent
    """
class ConversationManager:

    def __init__(self):
        self.router = IntentRouter()
        self.state_manager = StateManager()
        self.rag_agent = RAGAgent()
        self.welcome_agent = WelcomeAgent()

        self.agents = {
            AgentType.GREETING: GreetingAgent(),
            AgentType.CONTACT: ContactAgent(),
            AgentType.LANGUAGE: LanguageAgent(),
            AgentType.PORTFOLIO: PortfolioAgent(),
            AgentType.RAG: self.rag_agent,
        }

    def handle(self, request: ChannelMessage) -> ChatResponse:
        state = self.state_manager.get_or_create(
            request.session_id
        )

        # NEW USER CHECK
        if len(state.history) == 0:
            response = self.welcome_agent.handle(
                request,
                state
            )
            state.history.append(
                f"Assistant: {response.answer}"
            )

            return response

        state.history.append(
            f"User: {request.message}"
        )

        route = self.router.route(request)
        state.current_agent = route.agent_type.value

        if route.language:
            state.language = Language(route.language)

        agent = self.agents.get(
            route.agent_type,
            self.rag_agent
        )

        if route.agent_type == AgentType.LANGUAGE:
            response = agent.handle(
                request,
                state,
                route
            )
        else:
            response = agent.handle(
                request,
                state
            )

        state.history.append(
            f"Assistant: {response.answer}"
        )
        response.session_id = state.session_id

        return response