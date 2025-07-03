import requests
import os
import json

url = 'https://api.github.com/repos/armbian/build/releases'  # замените на нужный URL
try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    first_item = next(iter(data), None)
    os.environ['CURRENT'] = json.dumps(first_item)
    os.environ['CURRENT_NAME'] = first_item['name']
    print(first_item['name'])
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')

with open('current.json') as s:
  current = json.load(s)
os.environ['CURRENT_NAME_IN_REPO'] = current[name]