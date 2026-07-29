def route_intent(state):

    intent = state["intent"]


    if intent == "greeting":
        return "greeting"


    elif intent == "portfolio":
        return "portfolio"


    elif intent == "contact":
        return "contact"


    else:
        return "portfolio"