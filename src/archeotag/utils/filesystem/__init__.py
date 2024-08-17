import logging
from archeotag.utils import archeolog
import fsspec
import os


def get_filesystem() -> fsspec.AbstractFileSystem:
    azure_storage_connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if azure_storage_connection_string:
        logging.info(f"Using Azure storage blob filesystem")
        filesystem = fsspec.filesystem("abfs")
    else:
        logging.warning("Azure storage credentials not found! Using local filesystem")
        filesystem = fsspec.filesystem("file")
    return filesystem
