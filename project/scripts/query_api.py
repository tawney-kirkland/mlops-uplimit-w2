import json

import requests

data = {"review": "I really don't like this product that much"}
headers = {"Content-Type": "application/json"}
response = requests.post(
    "http://127.0.0.1:8000/predict", data=json.dumps(data), headers=headers
)
print(response.status_code, response.json())
