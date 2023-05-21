import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
#123345
print(response.text)