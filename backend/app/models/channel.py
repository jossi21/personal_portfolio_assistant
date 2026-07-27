from pydantic import BaseModel


class ChannelMessage(BaseModel):
    user_id: str
    channel: str
    message: str
    session_id: str | None = None