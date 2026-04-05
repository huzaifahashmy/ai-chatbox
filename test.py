import openai
from openai import OpenAI

from secret_key import secret_key
OpenAI.api_key = secret_key



client = OpenAI()

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain DSA in simple words"}
    ]
)

print(response.choices[0].message.content)