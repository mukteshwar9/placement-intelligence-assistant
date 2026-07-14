from langchain_community.document_loaders import PyPDFLoader
import os

class PDFLoader:
    def __init__(self, folder_path):
        self.folder_path=folder_path
    
    def load_documents(self):
        documents = []
        for file in os.listdir(self.folder_path):
            if file.endswith(".pdf"):
                pdf_path = os.path.join(self.folder_path, file)
                loader = PyPDFLoader(pdf_path)
                docs = loader.load()

                documents.extend(docs)

        return documents