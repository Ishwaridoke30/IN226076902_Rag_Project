from src.retriever import retrieve_docs
from src.embedding import embed_query

def get_answer(question):
    docs = retrieve_docs(question)
    
    if not docs:
        return "No relevant data found"

    return " ".join(docs)