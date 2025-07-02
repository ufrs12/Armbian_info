import requests
import os
import json

url = 'https://api.github.com/repos/armbian/build/releases'  # замените на нужный URL

rs =""
try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    print(data)
    rs = data
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')

obj = json.loads(rs)
names = find_all_names(obj)
print(names)

def find_all_names(obj):
    names = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "name":
                names.append(str(v))
            else:
                names.extend(find_all_names(v))
    elif isinstance(obj, list):
        for item in obj:
            names.extend(find_all_names(item))
    return names

obj = json.loads(data)
names_list = find_all_names(obj)
result_str = ", ".join(names_list)
print(result_str)  # Alice, Bob, Charlie

url = 'https://api.telegram.org/bot' + os.environ.get('TG_KEY') + '/sendmessage?chat_id=' + os.environ.get('TG_CHANNEL_ID') + '&text=' + result_str
try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    print(data)
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')
