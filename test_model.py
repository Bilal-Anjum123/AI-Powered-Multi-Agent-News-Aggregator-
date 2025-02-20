import requests

# Define the API endpoint
api_url = 'http://202.163.113.148:11434/api/generate'

# Define the model and input prompt
model_name = 'deepseek-r1:32b'  # Replace with the model you want to use
prompt = 'Hello, how are you?'

# Define the request payload
payload = {
    'model': model_name,
    'prompt': prompt,
    'stream': False  # Set to True if you want streaming responses
}

try:
    # Send the POST request
    response = requests.post(api_url, json=payload)
    response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)

    # Parse the JSON response
    result = response.json()
    print("Generated Response:", result['response'])

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.JSONDecodeError as json_err:
    print(f"JSON decode error: {json_err}")
    print("Raw response:", response.text)
except Exception as err:
    print(f"An error occurred: {err}")