# Import the requests library to handle HTTP requests
import requests

# Define a function to fetch the todos from the given URL
def fetch_todos():
    # Set the URL where the todos data is available
    url = "https://jsonplaceholder.typicode.com/todos"
    
    # Send a GET request to the URL and store the response
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python list of dictionaries
        todos = response.json()
        
        # Print a header to indicate we are displaying the first 10 todos
        print("First 10 TODOs:")
        
        # Loop through the first 10 todo items and print their details
        for todo in todos[:10]:
            # Print the ID, title, and completed status of each todo item
            print(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    else:
        # If the request failed, print an error message with the status code
        print(f"Failed to fetch todos. Status code: {response.status_code}")

# This block ensures the fetch_todos function runs only if this script is executed directly
if __name__ == "__main__":
    fetch_todos()
