import pymupdf
import pymupdf4llm
from tqdm import tqdm
import logging
from archeotag.utils import archeolog


def is_scanned_document(md_text):
    characters_found = set([c for c in md_text if not c.isspace()])
    return characters_found == {"-"}


def pdf2markdown(data: bytes, language: str = "ces") -> str:
    document = pymupdf.open("pdf", data)
    md_text = pymupdf4llm.to_markdown(document)
    if is_scanned_document(md_text):
        logging.info(f"Document is a scanned document, no text layer. Applying OCR")
        md_text = scanned2markdown(data, language=language)
    return md_text


def scanned2markdown(data: bytes, language: str = "ces") -> str:
    document = pymupdf.open("pdf", data)
    ocr_doc = pymupdf.open()
    pages = list(document.pages())
    for page in tqdm(pages):
        pixmap = page.get_pixmap()
        with pymupdf.open("pdf", pixmap.pdfocr_tobytes(language=language)) as imgpdf:
            ocr_doc.insert_pdf(imgpdf)
    md_text = pymupdf4llm.to_markdown(ocr_doc)
    return md_text
