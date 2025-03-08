# 📜 RAG-Based Summarizer with QnA Chatbot

## 🚀 Overview
This project is an AI-powered **RAG-Based Summarizer** that can extract and summarize content from various sources, including:
- **YouTube Videos** (via transcription)
- **PDF Documents** (with text and image OCR extraction)
- **Websites**

It also features a **RAG-Based QnA Chatbot**, allowing users to ask questions based on the extracted text or summary.

Users can choose different **LLMs** for summarization and QnA, leveraging **Groq AI** with LangChain.

## 🎯 Features
✅ **Multi-source Summarization:** Extract and summarize text from YouTube, PDFs, and websites.  
✅ **LLM Selection:** Choose from Llama-3-70B, Llama-3-8B, or Mixtral models.  
✅ **OCR Support:** Extract text from images in PDFs.  
✅ **RAG-Based QnA Chatbot:** Chat with either the extracted text or the summary.  
✅ **ChromaDB Integration:** Stores vectorized text for retrieval-augmented generation.  
✅ **Analytics Dashboard:** View summarization statistics, word count, and token usage.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo-url.git
cd your-project-folder
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys
Create a `.env` file and add your **Groq AI API Key**:
```
GROQ_API_KEY=your_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

---

## 🏗️ Project Structure
```
📂 project-folder/
│── 📜 app.py                     # Streamlit UI
│── 📂 modules/                   # Core functionalities
│   │── summarizer.py             # Summarization logic
│   │── youtube_extractor.py      # Extract YouTube transcripts
│   │── pdf_extractor.py          # Extract text & images from PDFs
│   │── web_extractor.py          # Extract text from websites
│   │── qna_bot.py                # RAG-based QnA chatbot
│   │── vector_store.py           # ChromaDB vector storage
│   │── llm_manager.py            # LLM selection & invocation
│── 📂 data/                      # Stores processed text & vectors
│── requirements.txt              # Dependencies
│── README.md                     # Project documentation
```

---

## 📝 Usage

### 🔹 Summarization
1️⃣ Choose a source: **YouTube, PDF, or Website**.  
2️⃣ Provide the **video URL, PDF file, or webpage URL**.  
3️⃣ Select an **LLM** (Llama-3-70B, Llama-3-8B, Mixtral).  
4️⃣ Click **Summarize** to generate a summary.

### 🔹 Chat with Extracted Text
1️⃣ Select **"Chat with Extracted Text"** mode.  
2️⃣ Ask questions about the original extracted content.

### 🔹 Chat with Summarized Content
1️⃣ Select **"Chat with Summary"** mode.  
2️⃣ Get answers based on the condensed summary.

---

## 🔥 Future Enhancements
- **Multi-document summarization**
- **Query-based summarization**
- **AI-generated key takeaways**
- **Voice input & AI speech response**
- **LLM cost & token estimation**

---

## 🤝 Contributing
1. Fork the repo & create a new branch.  
2. Implement changes & commit with meaningful messages.  
3. Open a pull request & describe your changes.  

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to modify and distribute it.

---


