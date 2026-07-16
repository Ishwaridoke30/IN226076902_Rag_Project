# RAG-Based Student Support Assistant

## Summary

The RAG-Based Student Support Assistant is an AI-powered application that helps students quickly find accurate answers from academic documents. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded PDF and text files and then generates context-aware responses using a Large Language Model (LLM). This reduces the time students spend searching through study materials and improves access to information.

---

## Background

Students often have to search through large amounts of study material to find answers to their questions. This process is time-consuming and can reduce productivity.

This project aims to solve these problems:

- Students spend too much time searching through notes and documents.
- Important information is difficult to locate quickly.
- Traditional keyword search often fails to understand the meaning of a question.
- Students need a simple AI assistant that can answer questions based on their own study materials.

The project uses Retrieval-Augmented Generation (RAG) so that answers are generated from uploaded documents rather than relying only on the language model's built-in knowledge.

---

## How is it used?

A student uploads one or more academic documents such as lecture notes, PDFs, or text files.

The system performs the following steps:

1. Loads the uploaded documents.
2. Splits the documents into smaller text chunks.
3. Creates vector embeddings for each chunk.
4. Stores the embeddings in a vector database.
5. Searches for the most relevant information when a question is asked.
6. Sends the retrieved information to the language model.
7. Returns an accurate, context-aware answer.

### Example

**Question:**

```
What is the attendance rule?
```

**Answer:**

```
The assistant retrieves the relevant section from the uploaded document and provides the correct attendance policy.
```

---

## Data sources and AI methods

### Data Sources

- Academic PDF documents
- Text files
- Student notes
- Course documentation

### AI Methods

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Similarity Search
- Large Language Models (LLMs)

### Technologies Used

- Python
- LangChain
- LangGraph
- ChromaDB / FAISS
- Hugging Face Embeddings
- OpenAI / LLM
- GitHub
- VS Code

---

## Challenges

Although the system provides useful answers, it has some limitations:

- The quality of answers depends on the uploaded documents.
- It cannot answer questions that are unrelated to the available documents.
- Incorrect or incomplete documents may produce inaccurate answers.
- Very large document collections may increase processing time.

---

## What next?

Future improvements include:

- Web interface using Streamlit or FastAPI
- Voice-based interaction
- Multi-language support
- Chat history
- User authentication
- Better document management
- Support for images and scanned PDFs
- Improved retrieval accuracy using advanced embedding models

---

## Project Structure

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


## Acknowledgments

This project was developed as part of learning Artificial Intelligence and Retrieval-Augmented Generation (RAG). It demonstrates how modern AI techniques can improve information retrieval and provide intelligent, context-aware assistance for students.

Special thanks to:

- Elements of AI / Building AI
- University of Helsinki
- Reaktor
- LangChain Community
- Hugging Face
