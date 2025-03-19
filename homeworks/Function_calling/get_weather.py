#Function calling example with get_weather function
# This example demonstrates how to call a function from a GPT-4 OpenAI model.
# The function is defined in the same file, but in a real-world scenario, you would call an external API to get the weather.
# The function takes a location as a parameter and returns the current temperature for that location.   
# Import the OpenAI class
from openai import OpenAI
import os
from dotenv import load_dotenv
from rich import print

load_dotenv()

# Create a client
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

# Define the function
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                }
            },
            "required": [
                "location"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]
# Call the function
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is the weather like in Paris today?"}],
    tools=tools
)

print(completion.choices[0].message.tool_calls)