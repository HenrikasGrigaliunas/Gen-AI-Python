from rich import print
import os 
from dotenv import load_dotenv
import requests
from openai import OpenAI
import json

load_dotenv()

openai_api_key = os.getenv("GITHUB_TOKEN")
if openai_api_key is None:
    print("Please set OPENAI_API_KEY in .env file")

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("[red]Error: siauliai.txt file not found[/red]")
        return None

def get_summary(text):

    client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=openai_api_key
)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                {"role": "user", "content": f"Please provide a concise summary of the following text:\n\n{text}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[red]Error during API call: {str(e)}[/red]")
        return None

def main():
    # Use absolute path to the file
    file_path = os.path.join(os.path.dirname(__file__), "siauliai.txt")
    content = read_file_content(file_path)
    
    if content:
        summary = get_summary(content)
        if summary:
            print("[green]Summary of the text:[/green]")
            print(summary)

if __name__ == "__main__":
    main()






