import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """Extracts text from an uploaded PDF file."""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in pdf_document])
    return text
