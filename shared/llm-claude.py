
import os
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def ask_claude(messages):

    res = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        messages=messages
    )

    #return res.content[0].text