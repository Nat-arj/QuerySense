import requests
from fastapi import HTTPException

def call_llm(prompt: str):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            },
            timeout=240
        )

        response.raise_for_status()

        return response.json()["response"]

    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=504,
            detail="LLM timeout"
        )

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=500,
            detail="LLM error"
        )