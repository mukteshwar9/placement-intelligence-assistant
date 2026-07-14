from src.loader import PDFLoader
from src.splitter import TextSplitter
from src.vector_store import VectorStore


def ingest_documents():
    print("Loading PDFs...")

    loader = PDFLoader("data")
    documents = loader.load_documents()

    print(f"Loaded {len(documents)} pages")

    splitter = TextSplitter()
    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    vector_store = VectorStore()

    db = vector_store.create_vector_store(chunks)

    db.save_local("vectorstore")

    print("Vector database saved successfully!")


if __name__ == "__main__":
    ingest_documents()