from pathlib import Path

from langchain_chroma import Chroma

from app.services.embedding_service import embedding_model



VECTOR_STORE_PATH = Path("app/vectorstore")



# Load existing vector database
vector_store = Chroma(
    persist_directory=str(VECTOR_STORE_PATH),
    embedding_function=embedding_model,
)



# Create retriever once
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
    },
)



def retrieve_documents(query: str):
    """
    Retrieve relevant documents from ChromaDB.
    """

    return retriever.invoke(query)