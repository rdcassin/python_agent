import os
from dotenv import load_dotenv
from google import genai

from utils import *

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages, user_prompt, verbose = read_input()

    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = messages,
    )

    agent_response(response, user_prompt, verbose)

if __name__ == "__main__":
    main()
