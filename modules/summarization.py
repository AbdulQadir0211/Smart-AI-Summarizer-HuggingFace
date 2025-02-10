from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve the Hugging Face API token
hf_api_token = os.getenv("HUGGINGFACE_API_KEY")

# Function to load the selected summarization model
def load_summarization_model(model_name):
    """Dynamically loads the selected LLM model."""
    return pipeline("summarization", model=model_name,use_auth_token=hf_api_token)

# Function to generate summary
def generate_summary(text, model_name):
    """Summarizes text using the selected model."""
    summarizer = load_summarization_model(model_name)
    return summarizer(text, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]

