import streamlit as st
import pandas as pd

def show_dashboard(summaries):
    st.title("📊 Summarization Analytics")
    
    df = pd.DataFrame(summaries, columns=["Source", "LLM Model", "Word Count", "Summary"])
    st.dataframe(df)

    st.bar_chart(df["Word Count"])



import streamlit as st
from modules.summarizer import summarize_content
from modules.youtube_extracter import transcribe_youtube
from modules.pdf_extractor import extract_text_from_pdf
from modules.web_extractor import extract_text_from_url
from modules.dashboard import show_dashboard

summaries = []

st.title("📜 RAG-Based Summarizer")

option = st.selectbox("Choose Source:", ["YouTube Video", "PDF Document", "Website"])
model_name = st.selectbox("Choose LLM:", ["Llama-3-70B", "Llama-3-8B", "Mixtral"])

if option == "YouTube Video":
    video_url = st.text_input("Enter YouTube URL:")
    if st.button("Summarize"):
        transcript = transcribe_youtube(video_url)
        summary = summarize_content(transcript, model_name)
        summaries.append(["YouTube", model_name, len(transcript.split()), summary])
        st.write(summary)

elif option == "PDF Document":
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    if pdf_file and st.button("Summarize"):
        text = extract_text_from_pdf(pdf_file)
        summary = summarize_content(text, model_name)
        summaries.append(["PDF", model_name, len(text.split()), summary])
        st.write(summary)

elif option == "Website":
    web_url = st.text_input("Enter Website URL:")
    if st.button("Summarize"):
        text = extract_text_from_url(web_url)
        summary = summarize_content(text, model_name)
        summaries.append(["Website", model_name, len(text.split()), summary])
        st.write(summary)

if st.button("Show Analytics"):
    show_dashboard(summaries)
