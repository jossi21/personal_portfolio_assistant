from typing import TypedDict, Optional, List
from app.models.chat import Action


class AgentState(TypedDict):

    message: str

    intent: Optional[str]

    response: Optional[str]

    actions: Optional[List[Action]]

    session_id: Optional[str]

    language: Optional[str]