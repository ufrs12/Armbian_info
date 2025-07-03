import requests
import os
import json

body = 'https://github.com/armbian/build/releases/tag/'
url = 'https://api.telegram.org/bot' + os.environ.get('TG_KEY') + '/sendmessage?chat_id=' + os.environ.get('TG_CHANNEL_ID') + '&text=' + os.environ['CURRENT_NAME'] + ' \n' + body + os.environ['CURRENT_NAME']
try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    print(data)
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')

with open('current.json', 'w', encoding='utf-8') as f:
    f.write(os.environ['CURRENT'])