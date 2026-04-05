from google import genai

# Initialize Gemini client with your API key
client = genai.Client(api_key="enter your API key here")

# List models
models = client.models.list()

for m in models:
    print(m.name)