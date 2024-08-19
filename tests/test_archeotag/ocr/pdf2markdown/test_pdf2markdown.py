import unittest
from archeotag.utils.filesystem import get_filesystem
from archeotag.ocr.pdf2markdown import pdf2markdown
import os
import tempfile

FILE_STORAGE = os.getenv("FILE_STORAGE")
FILESYSTEM = get_filesystem()


def check_exists(filesystem, file, msg):
    if not filesystem.exists(file):
        raise unittest.SkipTest(f"Test file {file} not found in file storage. {msg}")


class ComponentDesignTests(unittest.TestCase):

    def test_pdf2markdown(self):
        TEST_FILE = (
            f"{FILE_STORAGE}/tests/ocr/pdf2markdown/1521152328669_CTX201100942.pdf"
        )
        check_exists(
            FILESYSTEM,
            TEST_FILE,
            "Skipping pdf2markdown test of digital-first document",
        )
        with FILESYSTEM.open(TEST_FILE, "rb") as f:
            data = f.read()
        md_text = pdf2markdown(data)
        self.assertIsInstance(
            md_text,
            str,
            msg="output of pdf2markdown function is Markdown formatted string",
        )
        self.assertEqual(
            md_text.split("\n")[0],
            "### Muzeum Cheb, p.o. Karlovarského kraje",
            msg="output of pdf2markdown function is Markdown formatted string",
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(f"{tmpdir}/test_markdown.md", "wb") as f:
                f.write(md_text.encode())

    def test_scanned_document(self):
        TEST_FILE = (
            f"{FILE_STORAGE}/tests/ocr/pdf2markdown/1529434615308_MTX196601639.pdf"
        )
        check_exists(
            FILESYSTEM, TEST_FILE, "Skipping pdf2markdown test of scanned document"
        )
        with FILESYSTEM.open(TEST_FILE, "rb") as f:
            data = f.read()
        md_text = pdf2markdown(data)
        self.assertIsInstance(
            md_text,
            str,
            msg="output of pdf2markdown function is Markdown formatted string",
        )
        characters_found = set([c for c in md_text if not c.isspace()])
        self.assertSetEqual(
            characters_found,
            {"-"},
            msg="Processing scanned document returns Markdown without any valid characters",
        )
