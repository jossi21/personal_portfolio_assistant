from pathlib import Path
from langchain_chroma import Chroma
from app.services.embedding_service import get_embedding_model


VECTOR_STORE_PATH = Path("app/vectorstore")


_vector_store = None
_retriever = None



def get_retriever():
    """
    Create Chroma retriever once and reuse it.
    """

    global _vector_store
    global _retriever


    if _retriever is None:

        embedding_model = get_embedding_model()


        _vector_store = Chroma(
            persist_directory=str(VECTOR_STORE_PATH),
            embedding_function=embedding_model,
        )


        _retriever = _vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 10,
            },
        )


    return _retriever



def retrieve_documents(query: str):
    """
    Retrieve relevant documents from ChromaDB.
    """

    retriever = get_retriever()

    documents = retriever.invoke(query)

    return documents