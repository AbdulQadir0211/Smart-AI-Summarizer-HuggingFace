
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
import os
import sys

# Load environment variables
load_dotenv()


hf_api_token = os.getenv("HUGGINGFACE_API_KEY")

def get_huggingface_llm(model_name="mistral-7b"):
    model = AutoModelForCausalLM.from_pretrained(model_name,use_auth_token=hf_api_token)
    tokenizer = AutoTokenizer.from_pretrained(model_name,use_auth_token=hf_api_token)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)