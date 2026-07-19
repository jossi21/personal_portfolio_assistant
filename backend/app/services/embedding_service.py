from langchain_huggingface import HuggingFaceEmbeddings

# define the business logic which can create models
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)