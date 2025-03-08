from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

DB_DIR = "chroma_db"

# Load embeddings model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_chroma_collection():
    """Loads or creates a ChromaDB collection."""
    return Chroma(persist_directory=DB_DIR, embedding_function=embedding_model)

def store_text(text, metadata):
    """Stores extracted text or summary as embeddings in ChromaDB."""
    chroma = get_chroma_collection()
    chroma.add_texts([text], metadatas=[metadata])

def retrieve_text(query, k=5):
    """Retrieves the most relevant texts from ChromaDB."""
    chroma = get_chroma_collection()
    results = chroma.similarity_search(query, k=k)
    return [doc.page_content for doc in results]
