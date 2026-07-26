from app.models.language import Language


def get_greeting_response(language):
    greetings = {
        Language.ENGLISH:
        "Hey there! 👋 I'm Yosef's AI assistant. Ask me about his projects, skills, experience, services, or contact.",

        Language.AMHARIC:
        "ሰላም! 👋 እኔ የዮሴፍ አዘነግ AI ረዳት ነኝ። ስለ ፕሮጀክቶቹ፣ ችሎታዎቹ፣ ልምዱ እና አገልግሎቶቹ ጠይቁኝ።",

        Language.TIGRINYA:
        "ሰላም! 👋 ኣነ ናይ ዮሴፍ ኣዘነግ AI ሓጋዚ እየ።",

        Language.AFAN_OROMO:
        "Akkam! 👋 Ani gargaaraa AI Yosef ti.",

        Language.SOMALI:
        "Salaan! 👋 Waxaan ahay kaaliyaha AI ee Yosef."
    }

    return greetings.get(language, greetings[Language.ENGLISH])


def get_language_changed_response(language):
    confirmations = {
        Language.ENGLISH: "Language changed to English.",
        Language.AMHARIC: "ቋንቋው ወደ አማርኛ ተቀይሯል።",
        Language.TIGRINYA: "ቋንቋ ናብ ትግርኛ ተቐይሩ።",
        Language.AFAN_OROMO: "Afaan gara Afaan Oromootti jijjiiramee jira.",
        Language.SOMALI: "Luqadda waxaa loo beddelay Soomaali.",
    }

    return confirmations.get(language, confirmations[Language.ENGLISH])


def get_select_language_response(language):
    prompts = {
        Language.ENGLISH: "Please select your language:",
        Language.AMHARIC: "እባክዎ ቋንቋዎን ይምረጡ:",
        Language.TIGRINYA: "በጃኹም ቋንቋኹም ምረጹ:",
        Language.AFAN_OROMO: "Maaloo afaan kee filadhu:",
        Language.SOMALI: "Fadlan dooro luqadaada:",
    }

    return prompts.get(language, prompts[Language.ENGLISH])