import subprocess
import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')

# Initialize Slack app and request handler
api = FastAPI()

# 2. Your custom endpoint
@api.get("/exec")
def custom_endpoint(api_key, command):
    if api_key != API_KEY:
        return "Invalid API key!"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return result


if __name__ == "__main__":
    # Start the Uvicorn server programmatically
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
