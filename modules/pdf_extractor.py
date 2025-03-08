from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = " ".join([page.extract_text() or "" for page in reader.pages])
    return text if text.strip() else "No extractable text found."

def extract_images_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_text = [pytesseract.image_to_string(img) for img in images]
    return " ".join(extracted_text)[:5000] if extracted_text else "No text found in images."


#print(extract_text_from_pdf("D:\AI_summarizer_RAG\Abdul_Qadir (Resume).pdf"))