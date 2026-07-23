from app.models.chat import ChatRequest, ChatResponse
from app.models.state import ConversationStateModel
from app.routes.intent_router import IntentRouter, AgentType

# Agents
from app.agents.rag_agent import RAGAgent
from app.agents.greeting_agent import GreetingAgent
from app.agents.contact_agent import ContactAgent

# state manager which create conversation state
from app.conversation.state_manager import StateManager
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
        
        # register agents
        self.agents = {
            AgentType.GREETING: GreetingAgent(),
            AgentType.CONTACT: ContactAgent(),
            AgentType.RAG: self.rag_agent,
        }


    # Handle an incoming chat request.  
    def handle(self, request: ChatRequest)-> ChatResponse:

        state = self.state_manager.get_or_create(request.session_id)
        state.history.append(
            f'User: {request.message}'
        )
        agent_type = self.router.route(request)
        state.current_agent = agent_type.value
        agent = self.agents.get(
            agent_type,
            self.rag_agent,
        )

        response = agent.handle(request)
        state.history.append(
            f'Assistant: {response.answer}'
        )
        response.session_id =state.session_id
        # print(state.history)

        return response