import unittest
from archeotag.utils.filesystem import get_filesystem
from adlfs.spec import AzureBlobFileSystem
from fsspec.implementations.local import LocalFileSystem
from unittest import mock
import os


class ComponentDesignTests(unittest.TestCase):

    def test_azure_filesystem(self):
        with mock.patch.dict(
            os.environ,
            {
                "AZURE_STORAGE_CONNECTION_STRING": "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://host.docker.internal:10000/devstoreaccount1;"
            },
        ):
            filesystem = get_filesystem()
        self.assertIsInstance(
            filesystem,
            AzureBlobFileSystem,
            msg="Application uses AzureBlobFileSystem if AZURE_STORAGE_CONNECTION_STRING environment variable is provided",
        )

    def test_local_filesystem(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            filesystem = get_filesystem()
        self.assertIsInstance(
            filesystem,
            LocalFileSystem,
            msg="If AZURE_STORAGE_CONNECTION_STRING environment variable is not provided, application uses local filesystem",
        )
