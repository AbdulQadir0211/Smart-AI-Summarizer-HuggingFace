from fastapi import FastAPI, UploadFile, Form
from modules.youtube_extracter import transcribe_youtube
from modules.pdf_extractor import extract_text_from_pdf, extract_images_from_pdf
from modules.web_extractor import extract_text_from_url
from modules.summarizer import summarize_content

app = FastAPI()

@app.post("/summarize/youtube")
async def summarize_youtube(video_url: str, model_name: str = "Llama-3-70B"):
    transcript = transcribe_youtube(video_url)
    summary = summarize_content(transcript, model_name)
    return {"summary": summary}

@app.post("/summarize/pdf")
async def summarize_pdf(file: UploadFile, model_name: str = "Llama-3-70B"):
    pdf_text = extract_text_from_pdf(file.file)
    summary = summarize_content(pdf_text, model_name)
    return {"summary": summary}

@app.post("/summarize/website")
async def summarize_website(url: str, model_name: str = "Llama-3-70B"):
    web_text = extract_text_from_url(url)
    summary = summarize_content(web_text, model_name)
    return {"summary": summary}
