import requests
import os
import json

url = 'https://api.github.com/repos/armbian/build/releases'  # замените на нужный URL
try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    os.environ['CURRENT'] = json.dumps(next(iter(data), None))
    os.environ['CURRENT_NAME'] = first_item['name']
    print(first_item['name'])
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')

#with open('../current.json') as s:
#  current = json.load(s)

#if name != current[name]:
#    body = 'https://github.com/armbian/build/releases/tag/'

#    url = 'https://api.telegram.org/bot' + os.environ.get('TG_KEY') + '/sendmessage?chat_id=' + os.environ.get('TG_CHANNEL_ID') + '&text=' + name + ' \n' + body + name
#    try:
#        response = requests.get(url)
#        response.raise_for_status()  # проверка успешности запроса (код 200)
#        data = response.json()       # парсим JSON из ответа
#        print(data)
#    except requests.RequestException as e:
#        print(f'Ошибка запроса: {e}')
#    except ValueError:
#        print('Ответ не содержит корректный JSON')
#else:
