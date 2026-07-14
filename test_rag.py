from src.vector_store import VectorStore
from src.retriever import Retriever
from src.chatbot import ChatBot

print("Loading Vector Database...")

db = VectorStore().load_vector_store()

print("Vector DB Loaded!")

retriever = Retriever(db)

bot = ChatBot()

question = input("\nAsk a question: ")

docs = retriever.retrieve(question)

context = "\n\n".join(
    [doc.page_content for doc in docs]
)

print("\nRetrieved Chunks:")
print("-" * 50)

for doc in docs:
    print(doc.page_content[:200])
    print()

print("-" * 50)

answer = bot.ask(
    context,
    question
)

print("\nAnswer:\n")

print(answer)