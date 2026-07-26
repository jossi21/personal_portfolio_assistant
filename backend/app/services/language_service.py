from app.services.ai_service import llm
from app.models.language import LANGUAGE_NAMES


def translate_response(text: str, language: str):

    language_name = LANGUAGE_NAMES.get(
        language,
        "English"
    )

    # Don't translate English
    if language == "English":
        return text

    prompt = f"""
You are a professional translator.

Translate the text below into {language_name}.

STRICT RULES:
- Return ONLY the translated text.
- Do NOT explain anything.
- Do NOT add introductions.
- Do NOT mention the target language.
- Do NOT answer the question.
- Preserve names, URLs, emails, technologies, and company names.

Text:
{text}
"""

    response = llm.invoke(prompt)

    return response.content.strip()