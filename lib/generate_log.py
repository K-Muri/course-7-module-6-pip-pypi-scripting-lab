from datetime import datetime
import os
import requests

def generate_log(data):
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt".strip()
    
    if os.path.exists(filename):
        print("File already exists")
        return
    
    elif type(data) == list:
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
        
        print(f"Log written to {filename}")
    else:
        raise ValueError("Data should be a list.")
        
generate_log(["User logged in", "User updated profile", "Report exported"])

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    print(f"Fetched Post Title: {post.get('title', 'No title found')}")