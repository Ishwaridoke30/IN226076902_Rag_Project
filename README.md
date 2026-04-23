** RAG-Based Student Support System**
🧠 Project Overview

This project is an AI-powered Student Support System based on Retrieval-Augmented Generation (RAG).
It helps users get accurate answers from uploaded documents like PDFs and text files using AI.

🎯 Project Objective

To build an intelligent system that:

Reads and processes documents (PDF/Text)
Retrieves relevant information from stored data
Generates accurate answers using AI (LLM)
Provides a simple query-based interface for students
⚙️ Technologies Used
Python 🐍
LangChain / LangGraph
Vector Database (FAISS / Chroma)
OpenAI / LLM Model
PDF Processing Libraries
📁 Project Structure
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
🚀 How It Works
User uploads or provides documents
System processes and splits text
Embeddings are created and stored in vector DB
User asks a question
System retrieves relevant data
AI generates final answer
💡 Example
User: What is attendance rule?
System: It retrieves document data and answers based on it.

📌 Future Improvements
Web UI integration
Chat history feature
Multi-language support
Faster retrieval system
👨‍💻 Author
Student Project – Internship Work
RAG-based AI Assistant System
