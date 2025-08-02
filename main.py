# First, we need an image that we want to process.
from services.computer_vision import get_text_from_file
from services.blob import blob_client

# image = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
resume = "https://hccdaocrfilestorage.blob.core.windows.net/files/resume.pdf"
results = get_text_from_file(resume)
print(results)

# Upload a file to the blob storage.
# file_path = input("Enter file path:")
# with open(file_path, "rb") as file:
#     data = file.read()
#     client = blob_client.upload_blob("resume.pdf", data)
#     print(client.url)
