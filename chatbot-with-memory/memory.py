from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os

def create_vectorstore():
    embeddings = OpenAIEmbeddings()
    return FAISS(embeddings.embed_query, embeddings)

def save_memory(vectorstore, path="faiss_index"):
    vectorstore.save_local(path)

def load_memory(path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(path, embeddings)
