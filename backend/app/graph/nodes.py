from app.agents.greeting_agent import GreetingAgent
from app.agents.portfolio_agent import PortfolioAgent
from app.agents.contact_agent import ContactAgent


greeting_agent = GreetingAgent()
portfolio_agent = PortfolioAgent()
contact_agent = ContactAgent()



def greeting_node(state):

    result = greeting_agent.handle(
        state["message"]
    )

    state["response"] = result.message
    state["actions"] = result.actions

    return state



def portfolio_node(state):

    result = portfolio_agent.handle(
        state["message"]
    )

    state["response"] = result.message
    state["actions"] = result.actions

    return state



def contact_node(state):

    result = contact_agent.handle(
        state["message"]
    )

    state["response"] = result.message
    state["actions"] = result.actions

    return state



def response_node(state):

    return state