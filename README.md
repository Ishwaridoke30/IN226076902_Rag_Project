# RAG-Based Student Support Assistant

An AI-powered Student Support System built using Retrieval-Augmented Generation (RAG). This project enables students to ask questions about academic documents and receive accurate, context-aware answers using Large Language Models (LLMs).

---

## 📖 Overview

The RAG-Based Student Support Assistant combines document retrieval with generative AI to provide reliable responses based on uploaded documents instead of relying only on the LLM's internal knowledge.

The system processes PDF and text documents, stores their embeddings in a vector database, retrieves the most relevant information, and generates context-aware answers.

---

## ✨ Features

- 📄 Upload and process PDF/Text documents
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering
- 📚 Context-aware responses
- ⚡ Fast document retrieval
- 🔄 Modular and scalable architecture

---

## 🎯 Objective

The objective of this project is to develop an intelligent assistant that helps students quickly find information from academic documents.

The assistant can:

- Read and process educational documents
- Retrieve relevant information
- Answer user queries using AI
- Reduce manual searching through documents

---

## 🛠️ Technologies Used

- Python
- LangChain
- LangGraph
- ChromaDB / FAISS
- Hugging Face Embeddings
- OpenAI / LLM
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```
RAG-Project/
│
├── data/
│   └── student.txt
│
├── docs/
│   ├── HLD.pdf
│   ├── LLD.pdf
│   ├── Project Objective.pdf
│   └── Technical Documentation.pdf
│
├── src/
│   ├── main.py
│   ├── loader.py
│   ├── retriever.py
│   ├── generator.py
│   └── utils.py
│
└── README.md
```

---

## ⚙️ Workflow

1. Load documents
2. Split documents into chunks
3. Generate embeddings
4. Store embeddings in ChromaDB/FAISS
5. Retrieve relevant chunks
6. Generate answers using an LLM
7. Return accurate responses to the user

---

## 💬 Example

**Question**

```
What is the attendance rule?
```
**Answer**

The system retrieves the relevant information from the uploaded document and generates an accurate answer using the language model.

## 🚀 Future Improvements

- Web application using Streamlit
- Voice-based interaction
- Multi-language support
- Chat history
- User authentication
- Support for multiple document formats



---

## ⭐ Acknowledgements

This project was developed for learning Retrieval-Augmented Generation (RAG), document retrieval, and AI-powered question answering using LangChain, LangGraph, and vector databases.
