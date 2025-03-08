from modules.vector_store import retrieve_text
from modules.llm_manager import get_llm

def answer_question(query, model_name, context_type="summary"):
    """Answers questions using retrieved text (summary or extracted text)."""
    relevant_texts = retrieve_text(query)

    if not relevant_texts:
        return "No relevant information found."

    llm = get_llm(model_name)
    
    prompt = f"Use the following information to answer the query:\n\n{relevant_texts}\n\nQuery: {query}"
    response = llm.invoke(prompt)
    
    return response.page_content if hasattr(response, "page_content") else str(response)
