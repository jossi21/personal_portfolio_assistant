from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from app.services.embedding_service import embedding_model




KNOWLEDGE_PATH = Path("app/knowledge")
VECTOR_STORE_PATH = Path("app/vectorstore")

# document reader function which read all files inside knowledge folder
def load_documents():
    documents = []

    for file in KNOWLEDGE_PATH.glob("**/*.md"):
        loader = TextLoader(str(file), encoding="utf-8")
        documents.extend(loader.load())
    return documents


# This function which create chunks from the read files
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # chunk the read documents 
    chunks = splitter.split_documents(documents)
    return chunks



# the function which create vector stores
def create_vector_store(chunks):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(VECTOR_STORE_PATH)
    )

    return vector_store


# test the function
if __name__ == "__main__":
    docs = load_documents()
    
    print(f"Loaded {len(docs)} document(s)\n")
    # for i, doc in enumerate(docs, start=1):
    #     print(f"Document {i} (source: {doc.metadata.get('source')})")
    #     print(doc.page_content)
    #     print("=" * 50)

    chunks = split_documents(docs)
    print(f"\nCreated {len(chunks)} chunk(s)\n")

    # for i, chunk in enumerate(chunks, start=1):
    #     print(f"Chunk {i} (source: {chunk.metadata.get('source')})")
    #     print(chunk.page_content)
    #     print("-" * 50)

    vector_store = create_vector_store(chunks)
    print("Vector database created successfully!")