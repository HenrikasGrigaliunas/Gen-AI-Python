# Description: This script is an example of how to use the Google AI API to generate text using the Gemini model.
import os
from google import genai
from google.genai import types

from dotenv import load_dotenv  
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


# Generate text using the Gemini model
def generate():
    client = genai.Client(
        api_key=gemini_api_key,
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""who are you"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""I am a large language model, trained by Google.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the weather like today in Paris"""),
            ],
        ),
    ]
    # Generate content
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
