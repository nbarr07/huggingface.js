from openai import OpenAI

client = OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key="api_token",
)

stream = client.chat.completions.create(
    model="<together alias for meta-llama/Llama-3.1-8B-Instruct>",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
    max_tokens=512,
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")