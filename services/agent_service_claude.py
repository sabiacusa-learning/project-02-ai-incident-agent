# 
from fastapi import FastAPI
import pandas as pd
from shared.llm import ask_claude

app = FastAPI()

def load_csv(file):
    return pd.read_csv(f"data/{file}")

@app.post("/investigate")
def investigate(payload: dict):

    query = payload["query"]

    logs = load_csv("logs.csv").to_dict()
    metrics = load_csv("metrics.csv").to_dict()
    deployments = load_csv("deployments.csv").to_dict()

    context = f"""
    INCIDENT:
    {query}

    LOGS:
    {logs}

    METRICS:
    {metrics}

    DEPLOYMENTS:
    {deployments}
    """

    response = ask_claude([
        {
            "role": "user",
            "content": context
        }
    ])

    return {
        "analysis": response
    }