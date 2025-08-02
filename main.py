from services.computer_vision import computer_vision_client

# First, we need an image that we want to process.
image = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"

# Then, we need to call the computer vision client to process the image.
response = computer_vision_client.read(image, raw=True)
result_id = response.headers["Operation-Location"].split("/")[-1]
