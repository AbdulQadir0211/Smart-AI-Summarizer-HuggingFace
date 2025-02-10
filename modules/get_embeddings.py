
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

def get_huggingface_llm(model_name="mistral-7b"):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)