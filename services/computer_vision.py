from dotenv import load_dotenv
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()

VISION_KEY = os.getenv("VISION_KEY")
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")
VISION_REGION = os.getenv("VISION_REGION")

credentials = CognitiveServicesCredentials(VISION_KEY)
computer_vision_client = ComputerVisionClient(VISION_ENDPOINT, credentials)
