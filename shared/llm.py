from huggingface_hub import InferenceClient
import os

HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
MODEL = os.getenv("HF_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")

client = InferenceClient(
    token=HF_TOKEN,
    model=MODEL,
)

def ask_llm(prompt: str) -> str:

    response = client.text_generation(
        prompt,
        max_new_tokens=800,
        temperature=0.3,
        top_p=0.9
    )

    return response