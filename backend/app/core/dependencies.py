from fastapi import Depends
from app.conversation.manager import ConversationManager
from app.services.channel_gateway import ChannelGateway

conversation_manager = ConversationManager()

def get_conversation_manager() -> ConversationManager:
    """
    Provide the ConversationManager instance.
    The same instance is reused across requests.
    """

    return conversation_manager

# Create gateway dependency
def get_channel_gateway(
        manager: ConversationManager = Depends(get_conversation_manager)
) -> ChannelGateway:
    return ChannelGateway(manager)