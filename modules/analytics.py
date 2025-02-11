import matplotlib.pyplot as plt
import streamlit as st

def show_summary_stats(original_text, summarized_text):
    """Generate and display summary statistics."""
    before_len = len(original_text.split())
    after_len = len(summarized_text.split())
    reduction = ((before_len - after_len) / before_len) * 100

    fig, ax = plt.subplots()
    ax.bar(["Original", "Summarized"], [before_len, after_len], color=['blue', 'green'])
    ax.set_ylabel("Word Count")
    st.pyplot(fig)

    st.write(f"**Word Reduction:** {reduction:.2f}%")
