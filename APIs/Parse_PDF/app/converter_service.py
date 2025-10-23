from docling.document_converter import DocumentConverter
import tempfile
from pathlib import Path

def convert_pdf_to_markdown(pdf_file) -> str:
    """
    Converts a PDF file to Markdown using docling.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf_file.read())
        tmp_path = Path(tmp.name)
    
    converter = DocumentConverter()
    doc = converter.convert(str(tmp_path)).document
    markdown_output = doc.export_to_markdown()

    return markdown_output
