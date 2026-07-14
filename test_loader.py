from src.loader import PDFLoader

loader = PDFLoader("data")

documents = loader.load_documents()

print("Program Started")
print(f"Total pages loaded: {len(documents)}")

if len(documents) == 0:
    print("❌ No PDF found inside data folder.")
else:
    print("\nFirst Page:\n")
    print(documents[0].page_content[:500])

    print("\nMetadata:\n")
    print(documents[0].metadata)