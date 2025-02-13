
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
import os
import sys

# Load environment variables
load_dotenv()


os.environ['hf_api_token'] = os.getenv("HUGGINGFACE_API_KEY")

def get_huggingface_llm(model_name="mistral-7b"):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)


