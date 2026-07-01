from backend.app.rag.ingestion.loader import PDFLoader
from backend.app.services.document_service import DocumentService

loader = PDFLoader(
    pdf_path="data/raw/tesla/annual_reports/tesla_annual_report_2025.pdf",
    company="Tesla",
    year=2025,
    source="10-K",
)

documents = loader.load()

print(f"Pages Loaded: {len(documents)}")

print()

# print(documents[0])

print("=" * 80)
print(documents[0].text[:1500])
print("=" * 80)

# saving the prcessed documents to a json file
DocumentService.save_documents(
    documents,
    "data/processed/tesla_2024_10k.json",
)