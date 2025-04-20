import os
from groq import Groq

client = Groq(api_key="GROQ_API_KEY")


# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_chat_response(prompt, system_message="You are a helpful assistant.", history=None):
    if history is None:
        history = []

    messages = [{"role": "system", "content": system_message}]
    for msg in history:
        messages.append({"role": "user", "content": msg})
    messages.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        model= "meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False
    )

    return completion.choices[0].message.content.strip()
