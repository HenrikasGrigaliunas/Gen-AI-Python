import os
from google import genai
from google.genai import types
from rich import print

from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
        api_key=gemini_api_key
    )

# Get the absolute path to the image
image_path = os.path.join(os.path.dirname(__file__), "Image1.jpg")

# Read the image file
with open(image_path, "rb") as f:
    image = f.read()

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        types.Part.from_bytes(data=image, mime_type="image/jpg"),
        "Please describe the appearance in Lithuanian from uploaded picture",
    ],
)

print(response.text)