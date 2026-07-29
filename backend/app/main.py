from fastapi import FastAPI
from app.routes import health, chat, conversation, language, telegram, whatsapp
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

# create the app 
app = FastAPI(
    title=settings.app_name
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://jossi-az-bot.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
# register the router
app.include_router(health.router)
app.include_router(chat.router)
app.include_router(conversation.router)
app.include_router(language.router)
app.include_router(telegram.router)
app.include_router(whatsapp.router)

# home page endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Personal Portfolio Assistant API"
    }