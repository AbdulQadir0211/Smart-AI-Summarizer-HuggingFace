import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LLM_MODELS = {
    "Llama-3-70B": "llama-3.3-70b-versatile",
    "Llama-3-8B": "llama-3.1-8b-instant",
    "Mixtral": "mixtral-8x7b-32768"
}

def get_llm(model_name):
    if model_name not in LLM_MODELS:
        raise ValueError(f"Model '{model_name}' not available.")
    return ChatGroq(model=LLM_MODELS[model_name], temperature=0.7)
