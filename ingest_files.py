import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()


def load_docs():
    documents = []
    for file in os.listdir("varsity_docs"):
        loader = PyPDFLoader("varsity_docs/" + file)
        documents.extend(loader.load())
    return documents


def update_document_source(documents):
    for document in documents:
        document.metadata["source"] = os.path.splitext(
            os.path.basename(document.metadata["source"])
        )[0]


def chunk_docs(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunked_documents = text_splitter.split_documents(documents)
    return chunked_documents


def persist_docs(chunked_documents) -> Chroma:
    db = Chroma.from_documents(
        documents=chunked_documents,
        embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
        persist_directory="./chroma_db",
    )
    return db


if __name__ == "__main__":
    documents = load_docs()
    update_document_source(documents)
    chunked_documents = chunk_docs(documents)
    persist_docs(chunked_documents)
