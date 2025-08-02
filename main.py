from services.computer_vision import computer_vision_client
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time

# First, we need an image that we want to process.
image = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"

# Then, we need to call the computer vision client to process the image.
response = computer_vision_client.read(image, raw=True)
operation_id = response.headers["Operation-Location"].split("/")[-1]

# Check again and again for the status of the operation, and if it's succeeded, we can get the result.
while True:
    result = computer_vision_client.get_read_result(operation_id)
    if result.status == OperationStatusCodes.succeeded:
        break
    time.sleep(1)

if result is None or result.status != OperationStatusCodes.succeeded:
    raise Exception("Failed to read the image")

for text_result in result.analyze_result.read_results:
    for line in text_result.lines:
        print(line.text)