GREETINGS = {"hi", "hello", "hey", "yo", "sup" "hiya", "good morning", "good afternoon", "good evening",
}

GREETING_RESPONSE = (
    "Hey there! 👋 I'm Yosef's AI assistant. "
    "Ask me anything about his projects, skills, "
    "experience, services, or how to get in touch with him."
)


THANKS = {"thanks","thank you", "thank u", "thx", "ty",
}

THANKS_RESPONSE = (
    "You're welcome! 😊 "
    "Feel free to ask me anything about Yosef's "
    "projects, skills, or experience."
)


def normalize_text(text: str) -> str:
    """
    Normalize user input.
    """
    return text.strip().lower().rstrip("!?.,")



def is_greeting(message: str) -> bool:
    """
    Check whether the message is a greeting.
    """

    normalized = normalize_text(message)

    return (
        normalized in GREETINGS
        or normalized.startswith("hi ")
        or normalized.startswith("hello ")
        or normalized.startswith("hey ")
    )



def is_thanks(message: str) -> bool:
    """
    Check whether the message is a thank-you message.
    """

    return normalize_text(message) in THANKS