
import os
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import SystemMessage, HumanMessage

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OpenRouter API key is missing!")

bot = ChatOpenRouter(
    model="openai/gpt-4o-mini",
    api_key=api_key,
    temperature=0.7,
)

messages = [
    SystemMessage(
        content="You are Ektha, a friendly and helpful AI chatbot."
    )
]

print("Ektha: Hello! I'm connected to AI.")
print("Ektha: Type 'bye' to exit.")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "bye":
        print("Ektha: Goodbye!")
        break

    if not user_input:
        continue

    messages.append(HumanMessage(content=user_input))

    try:
        response = bot.invoke(messages)
        print("Ektha:", response.content)
        messages.append(response)

    except Exception as error:
        messages.pop()
        print("Error:", error)