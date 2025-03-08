from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

DB_DIR = "chroma_db"

# Load embeddings model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Text Splitter Configuration
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Adjust based on your needs
    chunk_overlap=50,  # Ensure some overlap to retain context
    separators=["\n\n", "\n", " ", ""],  # Prioritize paragraph, line, then word splits
)

def get_chroma_collection():
    """Loads or creates a ChromaDB collection."""
    return Chroma(persist_directory=DB_DIR, embedding_function=embedding_model)

def store_text(text, metadata):
    """Splits and stores extracted text or summary as embeddings in ChromaDB."""
    chroma = get_chroma_collection()
    
    # Split text into chunks
    text_chunks = text_splitter.split_text(text)
    
    # Store each chunk in ChromaDB
    chroma.add_texts(text_chunks, metadatas=[metadata] * len(text_chunks))

def retrieve_text(query, k=5):
    """Retrieves the most relevant texts from ChromaDB."""
    chroma = get_chroma_collection()
    results = chroma.similarity_search(query, k=k)
    return [doc.page_content for doc in results]
