from src.loader import PDFLoader
from src.splitter import TextSplitter
from src.vector_store import VectorStore
from src.retriever import Retriever

loader = PDFLoader("data")
documents = loader.load_documents()

splitter = TextSplitter()
chunks = splitter.split_documents(documents)

db = VectorStore().create_vector_store(chunks)

retriever = Retriever(db).get_retriever()

results = retriever.invoke("What is the CGPA requirement?")

for i, doc in enumerate(results):
    print("=" * 50)
    print(f"Result {i+1}")
    print(doc.page_content[:300])