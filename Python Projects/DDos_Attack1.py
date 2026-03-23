import requests

# Replace with your test server URL
url = "http://www.instagram.com/"

for i in range(500):
    try:
        response = requests.get(url)
        print(f"Request {i + 1}: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")