import requests
import os
import json

url = 'https://api.github.com/repos/armbian/build/releases'  # замените на нужный URL

try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    first_item = next(iter(data), None)
    print(first_item)
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')

url = 'https://api.telegram.org/bot' + os.environ.get('TG_KEY') + '/sendmessage?chat_id=' + os.environ.get('TG_CHANNEL_ID') + '&text=' + str(first_item)
try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    print(data)
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')
