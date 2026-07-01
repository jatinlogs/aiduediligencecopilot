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

embedded_chunks = embedding_service.embed_chunks(
    chunks[:5]
)

print(f"Chunks: {len(embedded_chunks)}")

print()

print(len(embedded_chunks[0].embedding))