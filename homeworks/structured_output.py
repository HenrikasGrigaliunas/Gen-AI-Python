import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv('GITHUB_TOKEN'),
)

completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed

print(event)