from enum import Enum


class AgentType(str, Enum):
    WELCOME = "welcome"
    GREETING = "greeting"
    CONTACT = "contact"
    PORTFOLIO = "portfolio"
    RAG = "rag"
    LANGUAGE = "language"