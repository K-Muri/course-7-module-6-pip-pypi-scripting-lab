from datetime import datetime
import os
import requests

def generate_log(data):
    if not isinstance(data, list):
        print("Error: Data must be a list")
        return False
    
    if len(data) == 0:
        print("Error: Data list cannot be empty")
        return False
    
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    try:
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
        
        print(f"✓ Log written to {filename}")
        print(f"  Location: {os.path.abspath(filename)}")
        print(f"  Entries: {len(data)}")
        return True
        
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def fetch_api_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            data = response.json()
            return [
                f"API Post Title: {data.get('title', 'No title')}",
                f"API Post Body: {data.get('body', 'No body')[:50]}..."
            ]
    except:
        return ["Failed to fetch API data"]
    return []


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        "Settings changed",
        "File uploaded"
    ]
    
    generate_log(log_data)
    
    print("\n--- Fetching API Data ---")
    api_data = fetch_api_data()
    if api_data:
        generate_log(api_data)