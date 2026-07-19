from fastapi import FastAPI
from app.routes import health, chat
from app.core.config import settings

# create the app 
app = FastAPI(
    title=settings.app_name
)

# register the router
app.include_router(health.router)
app.include_router(chat.router)

# home page endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Personal Portfolio Assistant API"
    }