from app.routes.intent_router import IntentRouter

intent_router = IntentRouter()

def intent_node(state):

    intent = intent_router.route(
        state["message"]
    )


    state["intent"] = intent.value


    return state