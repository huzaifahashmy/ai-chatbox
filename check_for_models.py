from google import genai

# ✅ Create client (NEW way)
client = genai.Client(api_key="AIzaSyBQQn0yMIDsfjLCslFH31VnVQtl5rm6yXs")

# ✅ List models
models = client.models.list()

for m in models:
    print(m.name)