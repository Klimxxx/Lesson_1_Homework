from json.decoder import JSONDecodeError
import requests

payload = {"name": "user"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
try:
    parsed_response_text = response.json()
    print(parsed_response_text["answer"])
except JSONDecodeError:
    print("Response is not a JSON format ")