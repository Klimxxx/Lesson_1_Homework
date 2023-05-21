import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
#123345456
print(response.text)