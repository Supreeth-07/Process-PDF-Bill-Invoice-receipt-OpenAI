from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from .converter_service import convert_pdf_to_markdown

app = FastAPI(
    title="PDF to Markdown Converter API",
    description="Convert PDF documents to Markdown using Docling",
    version="1.0.0",
)

@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file and get its Markdown conversion.
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    try:
        markdown_text = convert_pdf_to_markdown(file.file)
        return JSONResponse(content={"markdown": markdown_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
