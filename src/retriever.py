class Retriever:

    def __init__(self, vector_db):
        self.vector_db = vector_db

    def retrieve(self, question, k=6):
        docs = self.vector_db.similarity_search(
            question,
            k=k
        )

        return docs