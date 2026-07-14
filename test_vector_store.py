from src.loader import PDFLoader
from src.splitter import TextSplitter
from src.vector_store import VectorStore

loader = PDFLoader("data")
documents = loader.load_documents()

splitter = TextSplitter()
chunks = splitter.split_documents(documents)

vector_db = VectorStore()
db = vector_db.create_vector_store(chunks)

print("Vector Store Created Successfully!")
print(db.index.ntotal)