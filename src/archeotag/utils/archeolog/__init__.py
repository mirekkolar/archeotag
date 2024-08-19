import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s ARCHEOTAG: %(message)s")
logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(
    logging.WARNING
)
