
### **📌 AI Summarizer with RAG**
🚀 **A powerful AI-based text summarization tool** using open-source LLMs (**Mistral, Gemma, LLaMA**) with **RAG-based Q&A**, Speech-to-Text, PDF summarization, and URL summarization.

---

## **📝 Features**
✅ **Multi-Model Support** – Choose from **Mistral, Gemma, or LLaMA** for summarization.  
✅ **File Upload Support** – Summarize **PDFs** and **text files**.  
✅ **Speech-to-Text** – Convert voice input to text using **Whisper**.  
✅ **URL Summarization** – Extract and summarize text from web pages.  
✅ **RAG-based Q&A Chatbot** – Ask questions based on summarized content.  
✅ **Vector Database Integration** – Uses **FAISS/ChromaDB** for storing and retrieving similar summaries.  
✅ **Fine-tuning Support** – Customize **Mistral/Gemma** models for domain-specific summarization.  
✅ **Secure API Key Handling** – Uses `.env` for **Hugging Face API key management**.  

---

## **⚡ Tech Stack**
- **Python**
- **Hugging Face Transformers**
- **LangChain** (for document processing & retrieval)
- **FAISS/ChromaDB** (for RAG-based Q&A)
- **Streamlit** (for the web UI)

- **BeautifulSoup** (for web scraping)

---

## **🚀 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/ai-summarizer-rag.git
cd ai-summarizer-rag
```

### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # For Mac/Linux
env\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Hugging Face API Token**
- Create a `.env` file in the project root.
- Add your Hugging Face API key inside `.env`:
```plaintext
HF_API_TOKEN=your_huggingface_api_token
```

---

## **🛠️ Usage**
### **Run the Web App**
```bash
streamlit run app.py
```

### **How to Use?**
1. **Select a model** (Mistral, Gemma, or LLaMA).
2. **Choose an input method**:
   - 📜 Paste Text
   - 📂 Upload PDF/Text file
   - 🎤 Use Speech-to-Text
   - 🌍 Enter a URL for summarization
3. **Click ‘Summarize’** and get a concise summary.
4. **(Optional) Use the RAG chatbot** to ask follow-up questions.

---

## **📌 Customization**
Want to enhance the project? Here are some ideas:
1. **Fine-tune models** on domain-specific datasets.
2. **Optimize summarization** with LangChain's chunking strategies.
3. **Add multilingual support** for summarization.
4. **Deploy the app** on **AWS/GCP/Streamlit Cloud**.

---

## **💡 Troubleshooting**
### **🔴 Error: “Access to gated repo is restricted”**
✅ **Solution:**  
1. **Request access** to the model: [Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)  
2. **Login with your Hugging Face API key:**
   ```bash
   huggingface-cli login
   ```

---

## **📜 License**
This project is **open-source** under the **MIT License**.

---

## **🙌 Contributing**
Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## **🔗 Connect with Me**
📧 **Email:** abdulkadir9929@example.com  
🔗 **LinkedIn:** [Your Profile](https://www.linkedin.com/in/abdul-qadir0/)  
🚀 **GitHub:** [Your GitHub](https://github.com/AbdulQadir0211)  

