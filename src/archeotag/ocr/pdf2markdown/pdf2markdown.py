import pymupdf
import pymupdf4llm


def pdf2markdown(data: bytes) -> str:
    document = pymupdf.open("pdf", data)
    md_text = pymupdf4llm.to_markdown(document)
    return md_text
