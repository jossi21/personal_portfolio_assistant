from pydantic import BaseModel


class ChannelMessage(BaseModel):
    user_id: str
    user_name: str | None = None
    channel: str
    message: str
    session_id: str | None = None