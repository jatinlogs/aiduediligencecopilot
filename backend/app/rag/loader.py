import pdfplumber

from backend.app.models.document import Document


class PDFLoader:
    def __init__(self,pdf_path: str,company: str,year: int,source: str,):
        self.pdf_path = pdf_path
        self.company = company
        self.year = year
        self.source = source

    def load(self):
        documents = []

        with pdfplumber.open(self.pdf_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                text = page.extract_text()

                if not text:
                    continue

                document = Document(
                    company=self.company,
                    year=self.year,
                    source=self.source,
                    page=page_number,
                    text=text,
                )

                documents.append(document)

        return documents