from datetime import datetime
import os

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list")
    
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    print(f"Log written to {filename}")
    return True