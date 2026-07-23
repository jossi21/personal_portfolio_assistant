from app.conversation.manager import ConversationManager
conversation_manager = ConversationManager()

def get_conversation_manager() -> ConversationManager:
    """
    Provide the ConversationManager instance.
    The same instance is reused across requests.
    """

    return conversation_manager