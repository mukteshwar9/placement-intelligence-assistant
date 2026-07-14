from src.loader import PDFLoader
from src.splitter import TextSplitter
loader=PDFLoader("data")
documents=loader.load_documents()
splitter=TextSplitter()
chunks=splitter.split_documents(documents)
print(f"Pages loaded: {len(documents)}")
print(f"Chunks created: {len(chunks)}")
if chunks:
    print("\nFirst Chunk:\n")
    print(chunks[0].page_content[:500])
    print("\nMetadata:\n")
    print(chunks[0].metadata)