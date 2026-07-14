import os
import shutil

from src.loader import PDFLoader
from src.splitter import TextSplitter
from src.vector_store import VectorStore


class PDFProcessor:

    def __init__(self):

        self.data_folder = "data"

    def process_uploaded_file(self, uploaded_file):

        # Create data folder if it doesn't exist
        os.makedirs(self.data_folder, exist_ok=True)

        file_path = os.path.join(
            self.data_folder,
            uploaded_file.name
        )

        # Save uploaded file
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Load PDF
        loader = PDFLoader(self.data_folder)

        documents = loader.load_documents()

        # Split
        splitter = TextSplitter()

        chunks = splitter.split_documents(documents)

        # Create Vector DB
        vector_store = VectorStore()

        db = vector_store.create_vector_store(chunks)

        db.save_local("vectorstore")

        return len(documents), len(chunks)