import camelot
import pandas as pd
from pathlib import Path

def extract_tables_as_dataframe(pdf_path: str, pages: str = "1", flavor: str = "lattice") -> pd.DataFrame:
    """
    Extracts tables from a PDF using Camelot and returns a combined DataFrame.
    - flavor: 'lattice' (with lines) or 'stream' (no lines)
    - pages: page numbers, e.g., "1", "1-3", "all"
    """
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")
    if pdf_file.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    tables = camelot.read_pdf(str(pdf_file), pages=pages, flavor=flavor)
    if not tables:
        raise ValueError("No tables found in the PDF.")

    combined_df = pd.concat([table.df for table in tables], ignore_index=True)
    return combined_df
