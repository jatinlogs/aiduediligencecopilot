from backend.app.database.qdrant_client import QdrantVectorDatabase
from backend.app.services.embedding_service import EmbeddingService
from backend.app.rag.chunker import Chunker
from backend.app.rag.ingestion.loader import PDFLoader

loader = PDFLoader(
    pdf_path="data/raw/tesla/annual_reports/tesla_annual_report_2025.pdf",
    company="Tesla",
    year=2025,
    source="10-K",
)

documents = loader.load()

chunker = Chunker()

chunks = chunker.chunk_documents(documents)

embedding_service = EmbeddingService()

embedded_chunks = embedding_service.embed_chunks(chunks)

db = QdrantVectorDatabase()

db.create_collection()

db.upload(embedded_chunks)

print("Upload Complete!")