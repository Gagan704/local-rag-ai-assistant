import ollama


MODEL_NAME = "gemma3"


def get_ai_response(message):
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":
    print("🤖 My AI Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            break

        answer = get_ai_response(user_message)

        print(f"AI: {answer}\n")