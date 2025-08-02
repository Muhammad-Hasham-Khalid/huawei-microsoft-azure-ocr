from typing import Dict, List
from dotenv import load_dotenv
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time

load_dotenv()

VISION_KEY = os.getenv("VISION_KEY")
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")
VISION_REGION = os.getenv("VISION_REGION")

credentials = CognitiveServicesCredentials(VISION_KEY)
computer_vision_client = ComputerVisionClient(VISION_ENDPOINT, credentials)

def get_text_from_file(image: str) -> Dict[str, List[str]]:
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

    results: Dict[str, List[str]] = {}
    for text_result in result.analyze_result.read_results:
        lines: List[str] = [line.text for line in text_result.lines]
        results[text_result.page] = lines

    return results