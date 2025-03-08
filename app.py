import streamlit as st
import pandas as pd
from modules.summarizer import summarize_content
from modules.youtube_extracter import transcribe_youtube
from modules.pdf_extractor import extract_text_from_pdf, extract_images_from_pdf
from modules.web_extractor import extract_text_from_url
from modules.llm_manager import get_llm
from modules.vector_store import store_text, retrieve_text
from modules.rag_qa import answer_question

# ✅ Ensure `st.set_page_config()` is at the top
st.set_page_config(page_title="📜 RAG-Based Summarizer & QnA Chatbot", layout="wide")

# UI Layout
st.title("📜 RAG-Based Summarizer & Chatbot")
st.sidebar.header("Settings")

# User Input
option = st.sidebar.selectbox("Choose Source:", ["YouTube Video", "PDF Document", "Website"])
model_name = st.sidebar.selectbox("Choose LLM:", ["Llama-3-70B", "Llama-3-8B", "Mixtral"])

summaries = []

# Summarization Workflow
if option == "YouTube Video":
    video_url = st.text_input("Enter YouTube URL:")
    if st.button("Summarize YouTube Video"):
        if video_url:
            transcript = transcribe_youtube(video_url)
            summary = summarize_content(transcript, model_name)
            summaries.append(["YouTube", model_name, len(transcript.split()), summary])

            # Store both extracted text and summary in ChromaDB
            store_text(transcript, {"type": "extracted_text"})
            store_text(summary, {"type": "summary"})

            st.subheader("📄 Summary:")
            st.write(summary)

elif option == "PDF Document":
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    extract_images = st.checkbox("Extract text from images in PDF (OCR)?")
    if st.button("Summarize PDF"):
        if pdf_file:
            text = extract_text_from_pdf(pdf_file)
            if extract_images:
                text += extract_images_from_pdf(pdf_file)

            summary = summarize_content(text, model_name)
            summaries.append(["PDF", model_name, len(text.split()), summary])

            # Store both extracted text and summary in ChromaDB
            store_text(text, {"type": "extracted_text"})
            store_text(summary, {"type": "summary"})

            st.subheader("📄 Summary:")
            st.write(summary)

elif option == "Website":
    web_url = st.text_input("Enter Website URL:")
    if st.button("Summarize Website"):
        if web_url:
            text = extract_text_from_url(web_url)
            summary = summarize_content(text, model_name)
            summaries.append(["Website", model_name, len(text.split()), summary])

            # Store both extracted text and summary in ChromaDB
            store_text(text, {"type": "extracted_text"})
            store_text(summary, {"type": "summary"})

            st.subheader("📄 Summary:")
            st.write(summary)

# 🔹 **RAG-Based QnA Chatbot**
st.sidebar.subheader("💬 Chat with Extracted Text / Summary")
chat_mode = st.sidebar.radio("Select Context:", ["Summary", "Extracted Text"])
query = st.sidebar.text_input("Ask a question:")

if st.sidebar.button("Get Answer"):
    context_type = "summary" if chat_mode == "Summary" else "extracted_text"
    response = answer_question(query, model_name, context_type)
    st.sidebar.subheader("🤖 AI Response:")
    st.sidebar.write(response)

# 📊 **Show Analytics Dashboard**
if st.sidebar.button("Show Analytics"):
    if summaries:
        st.sidebar.subheader("📊 Summarization Analytics")
        df = pd.DataFrame(summaries, columns=["Source", "LLM Model", "Word Count", "Summary"])
        st.sidebar.dataframe(df)
        st.sidebar.bar_chart(df["Word Count"])
    else:
        st.sidebar.warning("No summaries available yet.")
