from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

# define chat request class which used to validate the input data which the user send to us
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

# Supported action types for the frontend
class ActionType(str, Enum):
    LINK = "link"
    BUTTON = "button"
    LANGUAGE = "language"
    REDIRECT = "redirect"

# Represents an interactive action return to the user
class Action(BaseModel):
    label: str
    type: ActionType
    value: str

# define chat response model used to validate and  formatted the response
# Standard response format for all agents
class ChatResponse(BaseModel):
    session_id: Optional[str] = None
    answer: str
    actions: Optional[List[Action]] = None