from backend.app.rag.loader import PDFLoader
from backend.app.rag.chunker import Chunker
from backend.app.services.storage_service import StorageService

loader = PDFLoader(
    pdf_path="data/raw/tesla/annual_reports/tesla_annual_report_2025.pdf",
    company="Tesla",
    year=2025,
    source="10-K",
)

documents = loader.load()

chunker = Chunker()

chunks = chunker.chunk_documents(documents)

print(f"Documents: {len(documents)}")
print(f"Chunks: {len(chunks)}")

print()

print(chunks[0])
#
print(chunks[1])

StorageService.save_chunks(chunks, "data/chunks/tesla_annual_report_2025_chunks.json")