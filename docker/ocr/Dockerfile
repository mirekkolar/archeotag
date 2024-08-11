FROM python:3.11

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-ces poppler-utils

RUN pip install \
    adlfs==2024.7.0 \
    fsspec==2024.6.1 \
    opencv-python==4.10.0.84 \
    pdf2image==1.17.0 \
    pymupdf==1.24.9 \
    Pillow==10.4.0 \
    pytesseract==0.3.10

COPY src /app/src
COPY pyproject.toml /app/pyproject.toml
RUN pip install /app
