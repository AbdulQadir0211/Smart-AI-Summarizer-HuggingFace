import pandas as pd

def generate_summary_report(summaries):
    """Generates a dataframe for summarization analytics."""
    return pd.DataFrame(summaries, columns=["Source", "LLM Model", "Word Count", "Summary"])
