import os
import time
import streamlit as st

from src.stats import Stats
from src.vector_store import VectorStore
from src.retriever import Retriever
from src.chatbot import ChatBot
from src.pdf_processor import PDFProcessor
from src.comparison import CompanyComparator

# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Placement Intelligence Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------
# Load CSS
# ---------------------------------

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.title("🤖 Placement Intelligence Assistant")

st.sidebar.success("🟢 AI Ready")

st.sidebar.caption("Retrieval-Augmented Generation")

st.sidebar.markdown("---")

pdfs = [f for f in os.listdir("data") if f.endswith(".pdf")]

st.sidebar.metric(
    "📄 Documents",
    Stats.get_document_count()
)



st.sidebar.markdown("---")

st.sidebar.subheader("📂 Uploaded PDFs")

if pdfs:
    for pdf in pdfs:
        st.sidebar.write(f"📄 {pdf.replace('.pdf','')}")
else:
    st.sidebar.info("No PDFs uploaded.")

st.sidebar.markdown("---")



if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()
# ---------------------------------
# Upload PDF
# ---------------------------------

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload Placement PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.sidebar.button("📚 Index Document"):

        progress = st.progress(0)

        progress.progress(20)

        processor = PDFProcessor()

        progress.progress(60)

        pages, chunks = processor.process_uploaded_file(
            uploaded_file
        )

        progress.progress(100)

        progress.empty()

        processor = PDFProcessor()

        pages, chunks = processor.process_uploaded_file(
            uploaded_file
        )

        st.sidebar.success(
            f"✅ Indexed {pages} pages into {chunks} chunks."
        )

        st.rerun()

# ---------------------------------
# Main Page
# ---------------------------------

st.markdown("""
# 🤖 Placement Intelligence Assistant

### AI-powered RAG chatbot for Placement Eligibility Documents

Ask questions, compare companies, and retrieve accurate answers from multiple placement PDFs.

---
""")

st.caption(
    "Ask questions using Retrieval-Augmented Generation (RAG)."
)

# ---------------------------------
# Load Vector Database
# ---------------------------------

try:

    db = VectorStore().load_vector_store()

    retriever = Retriever(db)

    bot = ChatBot()

except Exception:

    st.warning(
        "Please upload and index a PDF first."
    )

    st.stop()

# ---------------------------------
# Chat History
# ---------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------------------------
# Chat Input
# ---------------------------------
st.subheader("🚀 Quick Questions")

col1, col2 = st.columns(2)

with col1:
    if st.button("📄 TCS Eligibility"):
        st.session_state.quick_question = "What is TCS eligibility?"

    if st.button("📊 Compare TCS & Infosys"):
        st.session_state.quick_question = "Compare TCS and Infosys"

with col2:
    if st.button("🎓 Minimum CGPA"):
        st.session_state.quick_question = "What is the minimum CGPA?"

    if st.button("💼 Selection Process"):
        st.session_state.quick_question = "What is the selection process?"
question = st.chat_input(
    "Ask a question..."
)

if "quick_question" in st.session_state:
    if question is None:
        question = st.session_state.quick_question
    del st.session_state.quick_question

if question:

    # Show user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Retrieve documents

    start = time.time()

    docs = retriever.retrieve(question)

    end = time.time()

    retrieval_time = round(end - start, 3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Generate Answer

    with st.spinner("🤖 Thinking..."):

        if question and "compare" in question.lower():

            prompt = CompanyComparator.create_prompt(
                question,
                docs
            )

            answer = bot.ask_prompt(prompt)

        else:

            answer = bot.ask(
                context,
                question
            )

    # Save assistant response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Display assistant response

    with st.chat_message("assistant"):

        st.markdown(f"""
        <div style="
        padding:18px;
        border-radius:10px;
        background:#1e293b;
        color:white;
        ">
        {answer}
        </div>
        """, unsafe_allow_html=True)

        st.caption(
            f"""
        Retrieved **{len(docs)}** chunks
        in **{retrieval_time:.3f} sec**
        """
        )

        with st.expander("📚 Sources"):

            for doc in docs:

                source = os.path.basename(
                    doc.metadata.get(
                        "source",
                        "Unknown"
                    )
                )

                source = source.replace(
                    ".pdf",
                    ""
                )

                page = (
                    doc.metadata.get(
                        "page",
                        0
                    ) + 1
                )

                st.success(
                    f"📄 {source} | Page {page}"
        )
chat_text = ""

for message in st.session_state.messages:
    chat_text += f"{message['role'].upper()}:\n{message['content']}\n\n"

st.download_button(
    label="📥 Download Chat",
    data=chat_text,
    file_name="chat_history.txt",
    mime="text/plain"
)
# ---------------------------------
# Footer
# ---------------------------------

st.markdown("---")

st.caption(
    "Version 1.0 | Placement Intelligence Assistant | © 2026"
)