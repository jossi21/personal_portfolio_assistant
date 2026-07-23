from app.conversation.state_manager import StateManager


manager = StateManager()


state1 = manager.get_or_create(None)

print("First state:")
print(state1)


state2 = manager.get_or_create(
    state1.session_id
)

print("\nSecond state:")
print(state2)


print("\nSame session?")
print(state1.session_id == state2.session_id)