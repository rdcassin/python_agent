import sys
from google.genai import types

def read_input():
    if len(sys.argv) < 2:
        print("Usage: uv run main.py <user_prompt>")
        exit(1)
    
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role = "user", parts = [types.Part(text = user_prompt)]),
    ]

    verbose = False
    if len(sys.argv) > 2:
        flag = sys.argv[2]
        if flag == "--verbose":
            verbose = True

    return messages, user_prompt, verbose

def agent_response(response, user_prompt, verbose):
    print(f"Response: {response.text}\n")

    prompt_token = response.usage_metadata.prompt_token_count
    response_token = response.usage_metadata.candidates_token_count

    if verbose:
        print(f"User prompt: {user_prompt}\n")
        print(f"Prompt tokens: {prompt_token}\n")
        print(f"Response tokens: {response_token}\n")
