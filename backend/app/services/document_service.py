import json
from pathlib import Path

from backend.app.models.document import Document


class DocumentService:

    @staticmethod
    def save_documents(documents, output_path):

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(output_path, "w", encoding="utf8") as f:

            json.dump(
                [doc.model_dump() for doc in documents],
                f,
                indent=4,
            )