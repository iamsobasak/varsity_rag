import os
from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

def load_docs():
    documents = []
    for file in os.listdir("varsity_docs"):
        loader = PyPDFLoader("varsity_docs/"+file)
        documents.extend(loader.load())
    return documents

def chunk_docs(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunked_documents = text_splitter.split_documents(documents)
    return chunked_documents

def persist_docs(chunked_documents) -> Chroma:
    db = Chroma.from_documents(chunk_docs=chunked_documents, embedding=OpenAIEmbeddings(model="text-embedding-3-small"), persist_directory="./chroma_db")
    return db

if __name__=="__main__":
    documents = load_docs()
    chunked_documents = chunk_docs(documents)
    persist_docs(chunked_documents)
    

