from app.models.chat import ChatResponse, ChatRequest, Action, ActionType

# Handles contact-related request
class ContactAgent:
    # Return contact information with clickable actions
    def handle(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(
            answer="You can contact Yosef through the following channels:",
            actions=[
                Action(
                    label="Email ",
                    type=ActionType.LINK,
                    value="mailto:azenegyosef@gmail.com"
                ),
                Action(
                    label="Email",
                    type=ActionType.LINK,
                    value="azenegyosef@gmail.com"
                ),Action(
                    label="LinkedIn ",
                    type=ActionType.LINK,
                    value="azenegyosef@gmail.com"
                ),Action(
                    label="Github",
                    type=ActionType.LINK,
                    value="https://github.com/jossi21"
                ),Action(
                    label="WhatApp",
                    type=ActionType.LINK,
                    value="https://api.whatsapp.com/send?phone=251925553491"
                ),Action(
                    label="Portfolio",
                    type=ActionType.LINK,
                    value="https://jossi-five.vercel.app/"
                )
            ]
        )