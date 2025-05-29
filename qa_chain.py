import asyncio
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# ✅ Fix for asyncio bug on Windows
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

def load_qa_chain(pdf_path: str):
    # Load and split PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(documents)

    # Use efficient CPU embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Lightweight CPU-based LLM
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)
    llm = HuggingFacePipeline(pipeline=pipe)

    from langchain.chains import RetrievalQA
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
