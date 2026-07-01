from backend.app.rag.ingestion.loader import PDFLoader


def test_loader_creation():
    loader = PDFLoader("sample.pdf")
    assert loader.pdf_path.name == "sample.pdf"