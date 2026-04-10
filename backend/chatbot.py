import requests
import os

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_bot_response(user_input: str) -> str:
    try:
        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            return "API key not configured."

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "mistralai/mistral-7b-instruct:free",
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        data = response.json()

        print("DEBUG:", data)  # helps if something fails

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        return "API Error: " + str(data)

    except Exception as e:
        return "Error: " + str(e)