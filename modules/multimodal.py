from paddleocr import PaddleOCR
ocr = PaddleOCR()

def extract_text_from_image(image_path):
    """Extract text from images using OCR."""
    results = ocr.ocr(image_path)
    text = " ".join([res[1][0] for res in results[0]])
    return text

def summarize_multimodal(image_path, text):
    """Combine image text & document text for summarization."""
    img_text = extract_text_from_image(image_path)
    combined_text = text + " " + img_text
    return combined_text
