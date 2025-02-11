from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from vector_db import retrieve_similar_summaries
from dotenv import load_dotenv
from transformers import pipeline
import os

load_dotenv()

# Retrieve the Hugging Face API token
hf_api_token = os.getenv("HUGGINGFACE_API_KEY")


# Load LLaMA Model (Change Model Name as Needed)
LLAMA_MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"  # or "meta-llama/Llama-3-8B"

llm_pipeline = pipeline(
    "text-generation",
    model=LLAMA_MODEL_NAME,
    token=hf_api_token,
    device=0,  # Use GPU if available
    model_kwargs={"temperature": 0.7, "max_length": 512}
)

llm = HuggingFacePipeline(pipeline=llm_pipeline)



def rag_qa(question):
    """Retrieves answers using RAG-based retrieval."""
    retrieved_docs = retrieve_similar_summaries(question)
    
    # Convert retrieved docs to retriever
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    
    # Define RAG Chain
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)
    
    return qa_chain.run(question)

# Example usage
question = "What is the role of embeddings in RAG?"
answer = rag_qa(question)
print("Answer:", answer)