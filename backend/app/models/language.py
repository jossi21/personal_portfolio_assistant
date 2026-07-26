from enum import Enum


class Language(str, Enum):
    ENGLISH = "English"
    AMHARIC = "አማርኛ"
    TIGRINYA = "ትግርኛ"
    AFAN_OROMO = "Afaan Oromoo"
    SOMALI = "Soomaali"


LANGUAGE_NAMES = {
    "English": "English",
    "አማርኛ": "Amharic",
    "ትግርኛ": "Tigrinya",
    "Afaan Oromoo": "Afaan Oromo",
    "Soomaali": "Somali",
}