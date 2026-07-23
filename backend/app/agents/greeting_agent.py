from app.models.chat import ChatRequest, ChatResponse
from app.services.chat_utils import GREETING_RESPONSE, is_greeting


# Handles greeting conversations.
class GreetingAgent:
    
    # Process greeting requests.
    def handle(self, request:ChatRequest)-> ChatResponse:
        

        if is_greeting(request.message):
            return ChatResponse(
                answer=GREETING_RESPONSE
            )
        return ChatResponse(
            answer="Hello! How can i help ypu today?"
        )
