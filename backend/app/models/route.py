from typing import Optional
from pydantic import BaseModel
from app.models.agent import AgentType

class RouteResult(BaseModel):
    agent_type: AgentType
    language: Optional[str] = None