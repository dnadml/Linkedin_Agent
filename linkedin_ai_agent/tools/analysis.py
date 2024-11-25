
import openai

def analyze_data(data):
    openai.api_key = "your_openai_api_key"
    prompt = f"Analyze the following LinkedIn profile data:\n{data}\nProvide insights."
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
