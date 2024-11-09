from pinecone import Pinecone
from langchain_community.retrievers import PineconeHybridSearchRetriever
from pinecone_text.sparse import BM25Encoder
import os
import nltk
nltk.download('punkt_tab')
import dotenv
from pinecone import Pinecone,ServerlessSpec
from langchain_google_genai import GoogleGenerativeAIEmbeddings


# index_name = "openai-large-embedding"
index_name = "curriculum-embeddings"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

dotenv.load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index(index_name)

# Instantiate the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
# print(f"Creating embeddings...{embeddings}")

# Instantiate the BM25 encoder
bm25encoder = BM25Encoder()
# print(f"Creating BM25 encoder...{bm25encoder}")

sentences = [
    "Apple is a tech company known for its iPhones and MacBooks.",
]

bm25encoder.fit(sentences)

retriever = PineconeHybridSearchRetriever(embeddings=embeddings, sparse_encoder=bm25encoder, index=index)
# print(retriever)

