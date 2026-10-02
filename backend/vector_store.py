from langchain_community.vectorstores import FAISS
from backend.embeddings import embeddings

def create_vector_store(chunks):
    return FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

def search_pdf(vector_db, question):
    return vector_db.similarity_search(
        question,
        k=3
    )