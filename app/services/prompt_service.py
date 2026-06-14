from app.services.intent_service import (detect_intent,detect_format,detect_tone)

def build_prompt(query: str, feedback: str | None):

    intent = detect_intent(query)
    format_type = detect_format(query)
    tone = detect_tone(query)

    # WRITING (emails, leave, messages)
    if intent == "writing" or ("leave" in query.lower()) or ("email" in query.lower()):

        base_prompt = f"""
You are a professional writing assistant.

Your task:
- Generate a {format_type} based on the user's input
- Write ONLY the final content

STRICT RULES:
- Do NOT explain anything
- Do NOT include headings like "Explanation"
- Do NOT include policy or extra text
- Keep the tone {tone}
"""

    # CONTENT (blogs, articles)
    elif intent == "content":

        base_prompt = f"""
You are a content writer.

Your task:
- Write a well-structured blog/article
- Keep it clear, engaging, and {tone}

STRICT RULES:
- Do NOT explain separately
- Do NOT add unnecessary notes
"""

    # PROMPT ENGINEERING
    elif intent == "llm":

        base_prompt = f"""
You are a prompt engineering expert.

Your task:
- Convert the user's input into a high-quality LLM prompt

STRICT RULES:
- Return only the prompt
- Do NOT explain anything
"""

    # QUERY OPTIMIZATION
    else:

        base_prompt = f"""
You are a Query Optimization Assistant.

IMPORTANT:
The user query is a natural language search query.
It is NOT a database query.
Do NOT convert it into SQL.

Your job is ONLY to improve the wording of the query.

TASK:
- Rewrite the query in simple, clear natural language
- Provide exactly 3 suggestions to improve the query

STRICT RULES:
- DO NOT generate SQL queries
- DO NOT write code
- DO NOT answer the query
- DO NOT explain technically
- ONLY rewrite in plain English

BAD EXAMPLE (DO NOT DO THIS):
SELECT * FROM cars WHERE price < 200000

GOOD EXAMPLE:
Optimized Query: Used cars under ₹200,000 in India
Explanation: Improved clarity and added context.

OUTPUT FORMAT (STRICT):

Optimized Query: <optimized_query>
Explanation: <one short line>

Suggestions:
- <suggestion 1>
- <suggestion 2>
- <suggestion 3>
"""

    # FINAL PROMPT
    prompt = base_prompt + f"""

User Input:
"{query}"
"""

    # HUMAN-IN-THE-LOOP (REFINEMENT)
    if feedback:
        prompt += f"""

The user wants to refine the result using this input:
"{feedback}"

Update:
- Optimized Query
- Explanation
- Suggestions

Follow the SAME format strictly.
"""

    return prompt