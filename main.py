import requests

payload = {"name": "user"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)