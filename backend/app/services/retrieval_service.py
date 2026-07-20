from pathlib import Path
from langchain_chroma import Chroma
from app.services.embedding_service import embedding_model

VECTOR_STORE_PATH = Path("app/vectorstore")

# used to open an existed database
vector_store = Chroma(
    persist_directory=str(VECTOR_STORE_PATH),
    embedding_function=embedding_model
)

# the function used to retrieve the data from the database
def retrieve_documents(query: str):
    vector_store = Chroma(
        persist_directory="app/vectorstore",
        embedding_function=embedding_model,
    )

    retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
    },
)

    results = retriever.invoke(query)

    # print("\n========== RETRIEVED ==========")

    # for i, doc in enumerate(results, start=1):
    #     print(f"\nDocument {i}")
    #     print(doc.metadata)
    #     print(doc.page_content)

    return results


