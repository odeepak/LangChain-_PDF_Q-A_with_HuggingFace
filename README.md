# LangChain PDF Q&A with HuggingFace (CPU)

![LangChain](https://raw.githubusercontent.com/hwchase17/langchain/main/docs/source/_static/langchain_logo.svg)

## Overview

This project is a simple question-answering application built with **LangChain** that allows users to upload a PDF document and ask questions about its content. It leverages open-source Hugging Face models and runs entirely on CPU — **no API keys or paid services required**.

---

## Features

- **Upload PDF files** via an easy web interface.
- Automatically **extract and chunk text** from PDFs.
- Use **semantic vector search** (via FAISS and HuggingFace embeddings) to find relevant document parts.
- Generate natural language answers using the **`google/flan-t5-base`** language model.
- Runs fully **locally on CPU** without requiring OpenAI or other API keys.
- Built with **LangChain** for modular and scalable NLP workflows.
- Simple UI powered by **Streamlit**.

---

## How It Works

1. **Upload PDF:** The user uploads a PDF file through the web interface.
2. **Load & Split:** The text is extracted and split into chunks to maintain context.
3. **Embeddings:** Each chunk is converted into a vector embedding using HuggingFace’s `hkunlp/instructor-base` model.
4. **Indexing:** Embeddings are stored and indexed with FAISS for fast similarity search.
5. **Retrieve & Answer:** When a user asks a question, the app retrieves relevant chunks from FAISS and passes them with the question to the `google/flan-t5-base` model to generate an answer.
6. **Display:** The answer is displayed back to the user in the Streamlit app.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Internet connection for initial model downloads

langchain_pDF_Q&A_with_HuggingFace/
│
├── app.py                # Streamlit frontend + app logic
├── qa_chain.py           # LangChain Q&A pipeline setup (PDF loader, embeddings, FAISS, LLM)
├── requirements.txt      # Python package dependencies
├── example.pdf           # Sample PDF (optional)
└── README.md  
Dependencies
Package	Purpose
langchain	Language model orchestration
transformers	Hugging Face model pipelines
huggingface_hub	Access models from Hugging Face Hub
pypdf	PDF text extraction
faiss-cpu	Vector similarity search
streamlit	Web UI framework

Notes & Limitations
CPU-only: Runs slower than GPU but suitable for small/medium PDFs.

Model size: google/flan-t5-base balances performance and CPU compatibility.

Embeddings: Uses hkunlp/instructor-base instruction embeddings for semantic search.

No persistence: Vectorstore is rebuilt each run — you can extend to save/load index for speed.

Single PDF: Current app supports one PDF at a time.

Future Improvements
Support multi-file uploads and combined indexing

Add chat history and context retention for multi-turn conversations

Implement answer source highlighting and confidence scores

Enable GPU acceleration and larger models for better performance

Add caching/persistence of vectorstore and models for faster startup

About LangChain
LangChain is a framework designed to simplify building applications powered by large language models. It helps chain together different components like document loaders, vector stores, retrievers, and LLMs to create scalable NLP pipelines.

License
This project is licensed under the MIT License.

### Setup

1. Clone the repo:

```bash
git clone https://github.com/odeepak89/langchain-hf-cpu-app.git
cd langchain-hf-cpu-app
