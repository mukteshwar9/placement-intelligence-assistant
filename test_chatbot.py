from src.chatbot import ChatBot

bot = ChatBot()

context = """
TCS requires 60% throughout academics.

Selection Process:

1 Aptitude Test

2 Technical Interview

3 HR Interview
"""

question = input("Ask a question: ")

answer = bot.ask(context, question)

print("\nAnswer:\n")

print(answer)