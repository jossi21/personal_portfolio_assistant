from enum import Enum


class AgentType(str, Enum):
    GREETING = "greeting"
    CONTACT = "contact"
    PORTFOLIO = "portfolio"
    RAG = "rag"
    LANGUAGE = "language"