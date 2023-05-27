import requests

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
print(response.text)
response2 = requests.post("https://playground.learnqa.ru/api/check_type", data={"param2":"value2"})
print(response2.text)