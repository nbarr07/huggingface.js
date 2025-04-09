from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="fireworks-ai",
    api_key="api_token",
)

stream = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image in one sentence."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
                    }
                }
            ]
        }
    ],
    max_tokens=500,
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")