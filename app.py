import streamlit as st
from modules.summarization import generate_summary
from modules.pdf_processing import extract_text_from_pdf
from modules.web_scrapping import extract_text_from_url
#from modules.speech_to_text import convert_speech_to_text
from modules.youtube_transcript import transcribe_youtube
from modules.vector_db import store_summary_in_db
from modules.rag_chatbot import rag_qa
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Retrieve the Hugging Face API token
hf_api_token = os.getenv("HUGGINGFACE_API_KEY")
#login(token=hf_api_token)

st.title("📄 AI Summarizer + RAG Chatbot")
st.write("Summarize text, PDFs, webpages, YouTube videos, and audio using open-source LLMs!")

# 🎯 Model Selection
model_options = {
    "Mistral-7B": "mistralai/Mistral-7B-Instruct-v0.3",
    "Gemma-7B": "google/gemma-7b",
    "LLaMA-3-8B": "meta-llama/Llama-3.3-70B-Instruct"
}
selected_model = st.selectbox("🔍 Choose a Model:", list(model_options.keys()))

# Input Type Selection
upload_option = st.radio("Choose input type:", ["Text", "PDF File", "Web URL", "YouTube Video"])

# Handling Text Input
if upload_option == "Text":
    user_text = st.text_area("Enter text to summarize:", height=150)

# Handling PDF Upload
elif upload_option == "PDF File":
    uploaded_file = st.file_uploader("Upload a PDF file:", type=["pdf"])
    if uploaded_file:
        user_text = extract_text_from_pdf(uploaded_file)

# Handling Web URL Input
elif upload_option == "Web URL":
    url = st.text_input("Enter webpage URL:")
    if url and st.button("Fetch Webpage"):
        user_text = extract_text_from_url(url)
        st.text_area("Extracted Text:", user_text, height=200)

# Handling YouTube Video
elif upload_option == "YouTube Video":
    youtube_url = st.text_input("Enter YouTube Video URL:")
    if youtube_url and st.button("Transcribe Video"):
        user_text = transcribe_youtube(youtube_url)
        st.text_area("Transcribed Text:", user_text, height=200)



# Summarize Button
if st.button("Summarize"):
    if user_text:
        model_name = model_options[selected_model]  # Get model ID
        summary = generate_summary(user_text, model_name)
        st.subheader("Summary:")
        st.write(summary)
        #store_summary_in_db(summary, source=upload_option)
    else:
        st.warning("Please provide input to summarize!")

# RAG Chatbot

st.subheader("💬 Ask Questions About the Summary")
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if question:
        answer = rag_qa(question)
        st.write("**AI Answer:**", answer)
    else:
        st.warning("Please enter a question!")
