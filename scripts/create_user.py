import requests

url = 'http://localhost:5000/users'
data = {
    "name": "Carlos",
    "email": "carlos@example.com"
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    try:
        response_data = response.json()
        print(response_data)
    except ValueError:
        print("Response is not in JSON format:", response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
