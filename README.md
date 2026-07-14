# 🤖 Placement Intelligence Assistant

> An AI-powered Retrieval-Augmented Generation (RAG) chatbot that answers placement-related queries from company eligibility documents using LangChain, FAISS, Hugging Face Embeddings, Groq Llama 3.3, and Streamlit.

---

## 📌 Overview

Placement Intelligence Assistant enables students to upload placement eligibility PDFs and interact with them using natural language.

Instead of manually searching through multiple documents, users can simply ask questions like:

- What is the eligibility criteria for TCS?
- What is the minimum CGPA required?
- Which companies allow backlogs?
- Compare TCS and Infosys eligibility.

The application retrieves relevant document chunks using semantic search and generates accurate responses using a Large Language Model (LLM).

---

## 🚀 Features

### 📄 Multi-PDF Support
- Upload multiple placement eligibility PDFs
- Automatic indexing into the vector database

### 🤖 AI Question Answering
- Ask questions in natural language
- Answers generated using Retrieval-Augmented Generation (RAG)

### 🔍 Semantic Search
- Uses FAISS Vector Database
- Retrieves the most relevant document chunks

### 🧠 HuggingFace Embeddings
- sentence-transformers/all-MiniLM-L6-v2

### ⚡ Groq LLM
- Llama 3.3 70B Versatile
- Fast response generation

### 📚 Source Citations
- Shows PDF name
- Shows page number

### 💬 Chat Interface
- Chat history
- Download conversation
- Clear chat option

### 📂 PDF Upload
- Upload and index new placement documents directly from the UI

### 📊 Dashboard
Displays:

- Number of PDFs
- Number of Pages
- Number of Chunks
- Embedding Model
- LLM Used

### 🆚 Company Comparison
Compare placement criteria between multiple companies.

Example:

> Compare TCS and Infosys eligibility.

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| LLM | Groq Llama 3.3 |
| AI Framework | LangChain |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Database | FAISS |
| PDF Loader | PyPDF |
| Environment | Python Virtual Environment |

---

# 📂 Project Structure

```text
placement-intelligence-assistant/

│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── style.css
│
├── data/
│   ├── tcs.pdf
│   └── infosys.pdf
│
├── src/
│   ├── chatbot.py
│   ├── comparison.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── pdf_processor.py
│   ├── retriever.py
│   ├── splitter.py
│   ├── stats.py
│   └── vector_store.py
│
└── vectorstore/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/placement-intelligence-assistant.git

cd placement-intelligence-assistant
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Application starts at

```
http://localhost:8501
```

---

# 💡 Example Questions

- What is the TCS eligibility?
- What is the minimum CGPA?
- Which companies allow backlogs?
- Compare TCS and Infosys.
- What is the selection process?
- Which company offers the highest package?

---

# 🧠 How It Works

```
User Question
      │
      ▼
Retriever (FAISS)
      │
      ▼
Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Groq Llama 3.3
      │
      ▼
Final Answer + Sources
```

---

# 📸 Screenshots

## Home Page

_Add screenshot here_

---

## Chat Interface

_Add screenshot here_

---

## PDF Upload

_Add screenshot here_

---

## Company Comparison

_Add screenshot here_

---

# 🔮 Future Enhancements

- Authentication
- Conversation Memory
- PDF Preview
- Voice Assistant
- OCR Support
- Analytics Dashboard
- Multi-language Support
- Deployment on Streamlit Cloud

---

# 📈 Resume Highlights

- Developed an AI-powered Placement Intelligence Assistant using Retrieval-Augmented Generation (RAG).
- Implemented semantic document retrieval using FAISS and Hugging Face embeddings.
- Integrated Groq Llama 3.3 for low-latency AI responses.
- Built an interactive Streamlit interface supporting multi-PDF upload, semantic search, and company comparison.
- Designed a modular architecture with LangChain, vector databases, and conversational AI components.

---

# 👨‍💻 Author

**Mani Mukteshwar Somayajula**

B.Tech Computer Science (Data Science)

CMR Technical Campus

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

# ⭐ If you like this project

Give it a ⭐ on GitHub.
