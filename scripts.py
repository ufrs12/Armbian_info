import requests

url = 'https://api.example.com/data'  # замените на нужный URL

try:
    response = requests.get(url)
    response.raise_for_status()  # проверка успешности запроса (код 200)
    data = response.json()       # парсим JSON из ответа
    print(data)
except requests.RequestException as e:
    print(f'Ошибка запроса: {e}')
except ValueError:
    print('Ответ не содержит корректный JSON')