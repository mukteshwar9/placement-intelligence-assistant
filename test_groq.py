from src.chatbot import ChatBot

bot = ChatBot()

answer = bot.ask(
    "The minimum CGPA required is 7.0",
    "What is the minimum CGPA?"
)

print(answer)