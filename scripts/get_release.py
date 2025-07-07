import requests
import os
import json

with open('current.json') as s:
  current = json.load(s)

url = 'https://api.github.com/repos/armbian/build/releases'  # замените на нужный URL

response = requests.get(url)
response.raise_for_status()  # проверка успешности запроса (код 200)
data = response.json()       # парсим JSON из ответа
first_item = next(iter(data), None)
    
github_env = os.environ.get('GITHUB_ENV')
if github_env:
    with open(github_env, 'a') as f:
        f.write(f"CURRENT={json.dumps(first_item)}\n")
        f.write(f"CURRENT_NAME={first_item['name']}\n")
        f.write(f"CURRENT_NAME_IN_REPO={current['name']}\n")
else:
    print("Error: GITHUB_ENV variable not found")
   
print('Переменная курент' + os.environ['CURRENT'])
print(first_item['name'])
