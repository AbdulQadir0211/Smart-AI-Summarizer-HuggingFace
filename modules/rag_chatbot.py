from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from vector_db import retrieve_similar_summaries

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
llm = HuggingFacePipeline.from_model_id(model_id=MODEL_NAME, task="text-generation")

def rag_qa(question):
    """Retrieves answers using RAG-based retrieval."""
    retrieved_docs = retrieve_similar_summaries(question)
    retriever = retrieved_docs.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA(llm=llm, retriever=retriever)
    return qa_chain.run(question)
