from langchain_groq import ChatGroq
from config import GROQ_API_KEY


class ChatBot:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0
        )

    def ask(self, context, question):

        prompt = f"""
You are an AI Placement Assistant.

Answer ONLY from the context below.

If the answer is not present, reply:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

        response = self.llm.invoke(prompt)

        return response.content

    def ask_prompt(self, prompt):

        response = self.llm.invoke(prompt)

        return response.content