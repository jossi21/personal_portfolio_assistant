from app.services.retrieval_service import retrieve_documents

def get_context(question: str)-> str:
    """
    Retrieve the most relevant knowledge from the vector database.
    """

    documents = retrieve_documents(question)
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    return context