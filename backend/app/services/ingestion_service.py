from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


from app.services.embedding_service import get_embedding_model



KNOWLEDGE_PATH = Path("app/knowledge")

VECTOR_STORE_PATH = Path("app/vectorstore")



def load_documents():
    """
    Load markdown files from knowledge folder.
    """

    documents = []


    for file in KNOWLEDGE_PATH.glob("**/*.md"):

        loader = TextLoader(
            str(file),
            encoding="utf-8"
        )

        documents.extend(
            loader.load()
        )


    return documents




def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )


    chunks = splitter.split_documents(
        documents
    )


    return chunks




def create_vector_store(chunks):
    """
    Create Chroma vector database.
    """

    embedding_model = get_embedding_model()


    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(VECTOR_STORE_PATH)
    )


    return vector_store




if __name__ == "__main__":


    documents = load_documents()


    print(
        f"Loaded {len(documents)} document(s)"
    )


    chunks = split_documents(
        documents
    )


    print(
        f"Created {len(chunks)} chunk(s)"
    )


    create_vector_store(
        chunks
    )


    print(
        "Vector database created successfully!"
    )