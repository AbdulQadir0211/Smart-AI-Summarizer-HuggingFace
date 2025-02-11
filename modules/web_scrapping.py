import requests
from bs4 import BeautifulSoup

'''def extract_text_from_url(url):
    """Scrapes main content from a webpage."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = "\n".join([p.get_text() for p in paragraphs])
    return text
    '''


from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from modules.get_embeddings import get_huggingface_llm

def get_vectorstore_from_url(url):
    # get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()
    
    # split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    
    # create a vectorstore from the chunks using HuggingFace embeddings
    vector_store = Chroma.from_documents(document_chunks, get_huggingface_ll())

    return vector_store



def extract_text_from_url(url):
    # get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()
    return document[0].page_content