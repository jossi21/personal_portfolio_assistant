from app.routes.intent_router import IntentRouter
from app.models.chat import ChatRequest

router = IntentRouter()

print(router.route(ChatRequest(message="Hello")))
print(router.route(ChatRequest(message="Show me your projects")))
print(router.route(ChatRequest(message="how can i contact Yosef")))
print(router.route(ChatRequest(message="Who is Yosef")))
print(router.route(ChatRequest(message="change language")))