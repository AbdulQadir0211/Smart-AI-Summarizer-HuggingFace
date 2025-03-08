import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Error fetching the webpage."

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join(p.text for p in paragraphs)[:5000]  # Limit for LLM processing


#print(extract_text_from_url("https://en.wikipedia.org/wiki/Shah_Rukh_Khan"))