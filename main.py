import json

# Исходный JSON-текст
json_string = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

# Распарсить JSON-текст
json_obj = json.loads(json_string)

# Получить значение свойства "message" второго сообщения
message = json_obj["messages"][1]["message"]

print(message) # Выведет "This is the second message"