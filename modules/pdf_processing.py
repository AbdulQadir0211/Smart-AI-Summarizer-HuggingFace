import fitz  # PyMuPDF for PDF text extraction
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    """Extract text from normal PDFs."""
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text")
    return text if text.strip() else None

def ocr_pdf(pdf_path):
    """Extract text from scanned PDFs using OCR."""
    images = convert_from_path(pdf_path)
    text = " ".join(pytesseract.image_to_string(img) for img in images)
    return text.strip()

def process_pdf(pdf_path):
    """Extract or OCR text, then summarize."""
    text = extract_text_from_pdf(pdf_path) or ocr_pdf(pdf_path)
    return text
