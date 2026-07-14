import os

class Stats:

    @staticmethod
    def get_document_count():

        return len(
            [
                f
                for f in os.listdir("data")
                if f.endswith(".pdf")
            ]
        )

    @staticmethod
    def get_page_count():

        total_pages = 0

        try:

            from src.loader import PDFLoader

            loader = PDFLoader("data")

            docs = loader.load_documents()

            total_pages = len(docs)

        except:

            pass

        return total_pages

    @staticmethod
    def get_chunk_count():

        try:

            from src.loader import PDFLoader
            from src.splitter import TextSplitter

            loader = PDFLoader("data")

            docs = loader.load_documents()

            splitter = TextSplitter()

            chunks = splitter.split_documents(docs)

            return len(chunks)

        except:

            return 0