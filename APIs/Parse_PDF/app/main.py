# from fastapi import FastAPI, File, UploadFile, HTTPException
# from fastapi.responses import JSONResponse
# from .converter_service import convert_pdf_to_markdown

# app = FastAPI(
#     title="PDF to Markdown Converter API",
#     description="Convert PDF documents to Markdown using Docling",
#     version="1.0.0",
# )

# @app.post("/convert")
# async def convert_pdf(file: UploadFile = File(...)):
#     """
#     Upload a PDF file and get its Markdown conversion.
#     """
#     if not file.filename.lower().endswith(".pdf"):
#         raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
#     try:
#         markdown_text = convert_pdf_to_markdown(file.file)
#         return JSONResponse(content={"markdown": markdown_text})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from .converter_service import convert_pdf_to_markdown_from_path

app = FastAPI(
    title="PDF to Markdown Converter API",
    description="Convert a PDF (via file path) to Markdown using Docling",
    version="1.0.0",
)

class FilePathRequest(BaseModel):
    file_path: str

@app.post("/convert")
async def convert_pdf(request: FilePathRequest):
    """
    Pass a local file path and get Markdown output.
    """
    try:
        markdown_text = convert_pdf_to_markdown_from_path(request.file_path)
        return {"markdown": markdown_text}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------- New Table Extraction Endpoint -----------

from .table_extractor import extract_tables_as_dataframe

@app.post("/extract_table")
async def extract_table(
    file_path: str,
    pages: str = Query("1", description="Page numbers to extract (e.g., '1', '1-3', 'all')"),
    flavor: str = Query("lattice", description="Extraction method: 'lattice' or 'stream'")
):
    """
    Extract tables from a PDF file and return them as JSON.
    """
    try:
        df = extract_tables_as_dataframe(file_path, pages, flavor)
        return {"rows": df.to_dict(orient="records")}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
