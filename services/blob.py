import os
from azure.storage.blob import BlobServiceClient

storage_container = os.getenv("STORAGE_CONTAINER")
storage_account = os.getenv("STORAGE_ACCOUNT")
storage_connection_string = os.getenv("STORAGE_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(
    storage_connection_string
)

blob_client = blob_service_client.get_container_client(storage_container)
