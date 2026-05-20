# This is the gateway service that receives incident reports and forwards them to the AI agent for investigation.
from fastapi import FastAPI
import requests

app = FastAPI()

AGENT_URL = "http://localhost:8001/investigate"

@app.post("/investigate")
def investigate(payload: dict):

    response = requests.post(AGENT_URL, json=payload)

    return response.json()