import requests
import json

# API Base URL
BASE_URL = "http://202.163.113.148:11434"

def get_available_models():
    """Fetches the list of available models from the API."""
    response = requests.get(f"{BASE_URL}/api/tags")
    
    if response.status_code == 200:
        try:
            data = response.json()
            models = [model["name"] for model in data.get("models", [])]  # Extract model names
            print("✅ Available Models:", models)
            return models
        except requests.exceptions.JSONDecodeError:
            print("❌ Error: API returned invalid JSON for models list!")
            print("Raw response:", response.text)
            return []
    else:
        print(f"❌ Error fetching models (Status {response.status_code}):", response.text)
        return []

def summarize_with_deepseek(text):
    """Summarizes text using the deepseek-r1:32b model."""
    model_name = "deepseek-r1:32b"
    url = f"{BASE_URL}/api/generate"

    payload = {
        "model": model_name,  # Use correct model
        "prompt": f"Summarize this: {text}",
        "max_tokens": 100
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("✅ Summary generated successfully!")
        try:
            result = response.json()  # Try to parse JSON response
            return result.get("summary", "No summary available")
        except requests.exceptions.JSONDecodeError:
            print("❌ Error: API returned invalid JSON for summary!")
            print("Raw response:", response.text)
            return "Error in summarization: Invalid response format"
    else:
        print(f"❌ Error in summarization (Status {response.status_code}):", response.text)
        return f"Error in summarization: {response.text}"

# Run test
if __name__ == "__main__":
    available_models = get_available_models()
    
    if "deepseek-r1:32b" in available_models:
        summary = summarize_with_deepseek("A new method for training generative AI models...")
        print("📝 Summary:", summary)
    else:
        print("❌ Model deepseek-r1:32b not found in API!")
