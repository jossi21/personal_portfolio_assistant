from typing import List, Optional
from pydantic import BaseModel, Field
from app.models.language import Language

# represents the current state ot a conversation
class ConversationStateModel(BaseModel):
    session_id: str
    language: Language = Language.ENGLISH
    current_agent: Optional[str] = None
    channel: str = "web"
    history: List[str] = Field(default_factory=list)