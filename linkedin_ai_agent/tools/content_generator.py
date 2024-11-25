
from anthropic import Client

def generate_content(analysis):
    client = Client(api_key="your_anthropic_api_key")

    strategy_prompt = f"Create a content strategy:\n{analysis}"
    strategy_response = client.completion(
        prompt=strategy_prompt,
        stop_sequences=["\n"],
        max_tokens=300
    )

    content_prompt = f"Write three LinkedIn posts:\n{strategy_response}"
    content_response = client.completion(
        prompt=content_prompt,
        stop_sequences=["\n"],
        max_tokens=500
    )

    return strategy_response, content_response
