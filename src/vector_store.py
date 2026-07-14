from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class VectorStore:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def create_vector_store(self, chunks):

        return FAISS.from_documents(
            chunks,
            self.embedding
        )

    def load_vector_store(self):

        return FAISS.load_local(
            "vectorstore",
            self.embedding,
            allow_dangerous_deserialization=True
        )