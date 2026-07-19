from pathlib import Path
from langchain_community.document_loaders import TextLoader


KNOWLEDGE_PATH = Path("app/knowledge")

def load_documents():
    documents = []

    for file in KNOWLEDGE_PATH.glob("**/*.md"):
        loader = TextLoader(str(file), encoding="utf-8")
        documents.extend(loader.load())
    return documents


# if __name__ == "__main__":
#     docs = load_documents()
#     print(f"Loaded {len(docs)} document(s)\n")

#     for doc in docs:
#         print(doc.metadata)
#         print(doc.page_content)
       