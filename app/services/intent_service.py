def detect_intent(query: str):
    q = query.lower()

    if "leave" in q or "email" in q or "letter" in q:
        return "writing"

    elif "blog" in q or "article" in q:
        return "content"

    elif "prompt" in q or "chatgpt" in q:
        return "llm"

    return "search"


def detect_format(query: str):
    q = query.lower()

    if "email" in q:
        return "email"

    elif "letter" in q:
        return "letter"

    elif "blog" in q:
        return "blog"

    return "text"


def detect_tone(query: str):
    q = query.lower()

    if "friendly" in q:
        return "friendly"

    elif "formal" in q:
        return "formal"

    return "professional"