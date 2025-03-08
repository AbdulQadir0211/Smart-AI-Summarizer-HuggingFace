from langchain.chains.summarize import load_summarize_chain
from modules.llm_manager import get_llm


from langchain.chains.summarize import load_summarize_chain
from modules.llm_manager import get_llm


'''def summarize_content(text, model_name):
    """Summarizes text using the selected LLM and ensures proper response formatting."""
    llm = get_llm(model_name)
    
    try:
        # 🔹 Use invoke to get the response
        response = llm.invoke(f"Summarize this content:\n\n{text}")

        # 🔹 Handle different response formats
        if isinstance(response, str):
            return response  # Direct string response

        elif hasattr(response, "content"):
            return response.content  # Extract content attribute

        elif hasattr(response, "page_content"):
            return response.page_content  # Some LLMs use page_content

        else:
            return str(response)  # Convert to string as fallback

    except Exception as e:
        return f"Error while summarizing: {str(e)}"

'''

from modules.vector_store import store_text
from langchain.chains.summarize import load_summarize_chain
from modules.llm_manager import get_llm

def summarize_content(text, model_name):
    """Summarizes text and stores it in ChromaDB."""
    llm = get_llm(model_name)
    response = llm.invoke(f"Summarize this content:\n\n{text}")
    
    summary = response.page_content if hasattr(response, "page_content") else str(response)
    
    # Store the summary in ChromaDB
    store_text(summary, {"type": "summary"})
    
    return summary
