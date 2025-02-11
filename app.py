import streamlit as st
from modules.summarization import generate_summary
from modules.pdf_processing import extract_text_from_pdf, ocr_pdf
from modules.web_scrapping import extract_text_from_url
from modules.youtube_transcript import transcribe_youtube
#from modules.vector_db import store_summary_in_db, retrieve_similar_summaries
#from modules.rag_chatbot import rag_qa
from modules.email_service import send_summary_via_email
from modules.multimodal import summarize_multimodal
from modules.analytics import show_summary_stats
from dotenv import load_dotenv
import os
import sys

# Load environment variables
load_dotenv()

# Retrieve API key
hf_api_token = os.getenv("HUGGINGFACE_API_KEY")

# 🎯 Model Selection
st.title("📄 AI Summarizer + RAG Chatbot")
st.write("Summarize text, PDFs, webpages, YouTube videos, and audio using open-source LLMs!")

model_options = {
    "Mistral-7B": "mistralai/Mistral-7B-Instruct-v0.3",
    "Gemma-7B": "google/gemma-7b",
    "LLaMA-3-8B": "meta-llama/Llama-3.3-70B-Instruct"
}
selected_model = st.selectbox("🔍 Choose a Model:", list(model_options.keys()))

# Input Type Selection
upload_option = st.radio("Choose input type:", ["Text", "PDF File", "Web URL", "YouTube Video", "Image"])

user_text = ""

# Handling Text Input
if upload_option == "Text":
    user_text = st.text_area("Enter text to summarize:", height=150)

# Handling PDF Upload (Normal & Scanned)
elif upload_option == "PDF File":
    uploaded_file = st.file_uploader("Upload a PDF file:", type=["pdf"])
    if uploaded_file:
        text = extract_text_from_pdf(uploaded_file) or ocr_pdf(uploaded_file)
        user_text = text
        st.text_area("Extracted Text:", user_text, height=200)

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

# Handling Image Summarization
elif upload_option == "Image":
    uploaded_image = st.file_uploader("Upload an Image:", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        user_text = summarize_multimodal(uploaded_image, "")
        st.text_area("Extracted Text:", user_text, height=200)

# Summarization Button
if st.button("Summarize"):
    if user_text:
        model_name = model_options[selected_model]  # Get model ID
        summary = generate_summary(user_text, model_name)
        st.subheader("📌 Summary:")
        st.write(summary)

        # Store summary in vector database
        #store_summary_in_db(summary, source=upload_option)

        # Show summary statistics
        if st.button("📊 Show Summary Analytics"):
            show_summary_stats(user_text, summary)

        # Email Feature
        email = st.text_input("📩 Enter your email to receive the summary:")
        if st.button("Send Summary via Email"):
            send_summary_via_email(summary, email)
            st.success("✅ Summary Sent!")
    else:
        st.warning("⚠️ Please provide input to summarize!")



# 🔍 Vector Search: Retrieve Similar Summaries
'''
st.subheader("🔍 Retrieve Similar Summaries")
search_query = st.text_input("Enter a topic to find similar summaries:")
if st.button("Search Summaries"):
    similar_summaries = retrieve_similar_summaries(search_query)
    if similar_summaries:
        for idx, summary in enumerate(similar_summaries):
            st.write(f"**Summary {idx+1}:**", summary)
    else:
        st.warning("No similar summaries found.")

'''
'''
# 💬 RAG Chatbot for Q&A
st.subheader("💬 Ask Questions About the Summary")
question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if question:
        answer = rag_qa(question)
        st.write("**AI Answer:**", answer)
    else:
        st.warning("⚠️ Please enter a question!")

'''