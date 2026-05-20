from fastapi import FastAPI
import pandas as pd
from shared.llm import ask_llm

app = FastAPI()

def load_csv(file):
    return pd.read_csv(f"data/{file}")

@app.get("/")
def root():
    return {"status": "Agent service running"}

@app.post("/investigate")

def investigate(payload: dict):
    query = payload["query"]
    logs = load_csv("logs.csv").to_dict()
    metrics = load_csv("metrics.csv").to_dict()
    deployments = load_csv("deployments.csv").to_dict()

    prompt = f"""
You are an expert Site Reliability Engineer.
Analyze the incident and find the root cause.

INCIDENT:
{query}

LOGS:
{logs}

METRICS:
{metrics}

DEPLOYMENTS:
{deployments}

Return:
1. Root cause
2. Evidence
3. Fix recommendation
"""

    analysis = ask_llm(prompt)

    return {
        "analysis": analysis
    }