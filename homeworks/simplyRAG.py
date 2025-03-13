import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from rich import print

load_dotenv()

client = OpenAI(
#  api_key=os.getenv("OPENAI_KEY")
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv('GITHUB_TOKEN')
)

information = "Lithuania is the best place to work and live. the nature is beautiful, cities are modern and green" #RAG information added

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Extract the event information"},
    {"role": "system", "content": "Work with this data " + information}, #requesting RAG
    {"role": "user", "content": "What do you know about Lithuania?"}
  ]
)

print(completion.choices[0].message.content)