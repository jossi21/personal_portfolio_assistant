import uuid
from app.models.state import ConversationStateModel

# Manages conversation state
class StateManager:

    # constructor
    def __init__(self):
        self.sessions: dict[str, ConversationStateModel] = {}

    # create a new conversation
    def create(self)-> ConversationStateModel:
        session_id = str(uuid.uuid4())
        state = ConversationStateModel(
        session_id=session_id
        )

        self.sessions[session_id] = state

        return state

    # retrieve an existing conversation state
    def get(self, session_id: str)-> ConversationStateModel | None:
        return self.sessions.get(session_id)

    # return existing state or create a new one
    def get_or_create(self, session_id: str | None
    )-> ConversationStateModel:
        if session_id:
            state = self.get(session_id)
            if state:
                return state

        return self.create()