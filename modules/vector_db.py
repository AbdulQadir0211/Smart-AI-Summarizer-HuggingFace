from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document  # Required for storing documents properly
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve the Hugging Face API token
hf_api_token = os.getenv("HUGGINGFACE_API_KEY")

# Load embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize FAISS with at least one document
sample_doc = [Document(page_content="This is a placeholder document.")]
vector_db = FAISS.from_documents(sample_doc, embeddings)

def store_summary_in_db(summary, source):
    """Stores summarized text in FAISS vector database."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.create_documents([summary])
    vector_db.add_documents(docs, metadatas=[{"source": source}])

def retrieve_similar_summaries(query):
    """Retrieves similar summaries from FAISS."""
    return vector_db.similarity_search(query, k=3)
