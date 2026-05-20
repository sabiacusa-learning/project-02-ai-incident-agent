📊 Incident Response Agent

An AI-powered incident investigation system that analyzes logs, metrics, and deployment data using Claude to generate root cause analysis (RCA) for production issues.
This project simulates a real-world observability + SRE assistant platform using a microservice-inspired architecture, CSV-based telemetry, and an LLM-driven reasoning engine.

🚀 Key Features
  * Claude-powered incident analysis (root cause reasoning)
  * CSV-based observability layer (logs, metrics, deployments)
  * Microservice-style architecture (Gateway, Agent, Retrieval, Tools)
  * Cross-source correlation (logs + metrics + deployments)
  * Incident timeline reconstruction
  * Streamlit-based investigation UI
  * FastAPI backend services (modular design)
  * Production-style architecture patterns 

🏗️ Architecture Overview 

System Design
<img width="966" height="236" alt="image" src="https://github.com/user-attachments/assets/52e445c9-34ad-4b83-b055-d20336333d32" />

⚙️ Tech Stack
* Frontend: Streamlit
* Backend: FastAPI
* AI Model: Anthropic Claude
* Data Layer: CSV (POC), extensible to Postgres + pgvector
* Architecture Style: Microservice-inspired modular backend

1. Install dependencies

python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn streamlit pandas requests anthropic python-dotenv

2. Start services
Terminal 1 — Agent Service
uvicorn services.agent_service:app --port 8001 --reload
Terminal 2 — API Gateway
uvicorn gateway.main:app --port 8000 --reload
Terminal 3 — UI
streamlit run ui/streamlit_app.py


