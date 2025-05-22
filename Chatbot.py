from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def chat(prompt):
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            break

        response = chat(user_input)
        print("\n\nCHAT:", response, "\n\n")
