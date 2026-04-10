import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_bot_response(user_input: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # cheap + fast
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return "Error: " + str(e)