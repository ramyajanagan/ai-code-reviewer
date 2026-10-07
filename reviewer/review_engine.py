import os
import httpx

SYSTEM_PROMPT = """You are an expert senior software engineer. Review the following Git diff. 
Identify potential bugs, security flaws, performance bottlenecks, and code style improvements.
Provide your response in concise, actionable bullet points."""

def analyze_diff(diff_text: str, api_key: str) -> str:
    """Send code diff to LLM API for analysis."""
    if not diff_text:
        return "No code changes detected in Git repository."

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Here is the diff:\n\n{diff_text}"}
        ],
        "temperature": 0.2
    }

    with httpx.Client(timeout=30.0) as client:
        response = client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
