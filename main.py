from src.loader import load_data
from src.chunker import chunk_data
from src.embedding import create_vectorstore
from src.retriever import retrieve
from src.rag_pipeline import generate_answer

# Load data
data = load_data()

# Chunk data
chunks = chunk_data(data)

# Create vector database
vectorstore = create_vectorstore(chunks)

# Query loop
while True:
    query = input("\nAsk your query (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    results = retrieve(query, vectorstore)
    answer = generate_answer(query, results)

    print("\n", answer)