from langgraph.graph import StateGraph, END

from app.graph.state import AgentState

from app.graph.intent_node import intent_node

from app.graph.nodes import (
    greeting_node,
    portfolio_node,
    contact_node
)

from app.graph.edges import route_intent



workflow = StateGraph(AgentState)



# Nodes

workflow.add_node(
    "intent",
    intent_node
)


workflow.add_node(
    "greeting",
    greeting_node
)


workflow.add_node(
    "portfolio",
    portfolio_node
)


workflow.add_node(
    "contact",
    contact_node
)



# Start

workflow.set_entry_point(
    "intent"
)



# Intent decides next node

workflow.add_conditional_edges(
    "intent",
    route_intent,
    {
        "greeting": "greeting",
        "portfolio": "portfolio",
        "contact": "contact"
    }
)



# Finish

workflow.add_edge(
    "greeting",
    END
)

workflow.add_edge(
    "portfolio",
    END
)

workflow.add_edge(
    "contact",
    END
)



assistant_graph = workflow.compile()