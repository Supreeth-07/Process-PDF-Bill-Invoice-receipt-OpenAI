# FILE UPLOAD CODE
# from docling.document_converter import DocumentConverter
# import tempfile
# from pathlib import Path

# def convert_pdf_to_markdown(pdf_file) -> str:
#     """
#     Converts a PDF file to Markdown using docling.
#     """
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
#         tmp.write(pdf_file.read())
#         tmp_path = Path(tmp.name)
    
#     converter = DocumentConverter()
#     doc = converter.convert(str(tmp_path)).document
#     markdown_output = doc.export_to_markdown()

#     return markdown_output

# USING FILE PATH CODE
from docling.document_converter import DocumentConverter
from pathlib import Path

def convert_pdf_to_markdown_from_path(pdf_path: str) -> str:
    """
    Converts a PDF file (given by path) to Markdown using docling.
    """
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")
    if pdf_file.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    converter = DocumentConverter()
    doc = converter.convert(str(pdf_file)).document
    markdown_output = doc.export_to_markdown()

    return markdown_output