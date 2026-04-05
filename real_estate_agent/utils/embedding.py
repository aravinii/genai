import chromadb
from chromadb import EmbeddingFunction
from utils.config import CLIENT, MODEL_EMBEDDING
from utils.config import DB_NAME, CHROMA_DB_PATH

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __init__(self, model=MODEL_EMBEDDING):
        self.model = model

    def __call__(self, input):
        response = CLIENT.models.embed_content(
            model=self.model,
            contents=input
        )
        return [e.values for e in response.embeddings]

def search_neighborhood_context(question: str, neighborhood: str, k: int = 5):
    """
    Retrieve top-k context chunks about a neighborhood from the vector database.
    """
    
    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    db = chroma_client.get_collection(name=DB_NAME, embedding_function=GeminiEmbeddingFunction())

    results = db.query(
        query_texts=[question],
        n_results=k,
        where={"neighborhood": neighborhood}
    )

    docs = results.get("documents", [[]])[0]

    if not docs:
        return "No context found for this neighborhood."

    context = "\n\n".join(docs)

    return context