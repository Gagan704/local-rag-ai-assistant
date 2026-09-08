# 🤖 Local AI Assistant with RAG

A local AI assistant built with Python, Ollama, Gemma 3, and Retrieval-Augmented Generation (RAG).

The application can answer general questions, maintain conversation history, and answer questions from uploaded PDF documents while providing the relevant source and page numbers.

## 🚀 Features

- Local LLM using Ollama + Gemma 3
- Retrieval-Augmented Generation (RAG)
- PDF document processing
- Multiple PDF support
- Semantic search using sentence embeddings
- Cosine similarity-based retrieval
- Source and page citations
- Persistent conversation memory
- Conversation clearing
- Gradio web interface
- PDF upload directly through the UI

## 🧠 How It Works

```text
User
  ↓
Gradio Interface
  ↓
Question Router
  ↓
 ┌───────────────────────┐
 │                       │
General Question      PDF Question
 │                       │
 ↓                       ↓
Gemma 3              Embedding Search
                         ↓
                    Relevant Chunks
                         ↓
                       Gemma 3
                         ↓
                  Answer + Sources



🛠️ Technologies

* Python
* Ollama
* Gemma 3
* Sentence Transformers
* Scikit-learn
* PyPDF
* Gradio


📄 RAG Pipeline

1. Upload a PDF.
2. Extract text page by page.
3. Split the document into smaller chunks.
4. Generate embeddings for each chunk.
5. Convert the user’s question into an embedding.
6. Calculate similarity between the question and document chunks.
7. Retrieve the most relevant chunks.
8. Send the retrieved context to Gemma 3.
9. Generate an answer based on the document.
10. Display the source PDF and page numbers.


💡 Why RAG?

Instead of relying only on the language model’s existing knowledge, the system retrieves relevant information from the user’s documents and provides that information as context to the model.
This helps the assistant answer questions about private or user-provided documents.


▶️ Running the Project

-Install dependencies
  pip install -r requirements.txt


-Start Ollama
Make sure Ollama is installed and the Gemma 3 model is available.
  ollama run gemma3

-Run the Notebook
Open the Jupyter Notebook in PyCharm and run the cells.
The final cell launches the Gradio interface.


📌 Example
Question:
What is the main objective of this project?

Answer:
The assistant retrieves relevant sections from the uploaded PDF and generates an answer using Gemma 3.
The response also includes the relevant PDF source and page numbers.


🔮 Future Improvements

* FastAPI backend
* Docker containerization
* Better document chunking
* Improved retrieval evaluation
* Authentication
* Support for additional document formats
* Production deployment