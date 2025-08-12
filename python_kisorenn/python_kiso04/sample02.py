import requests

url = "https://v2.jokeapi.dev/joke/Any"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data['type'] == 'single':
        print("ジョーク:", data['joke'])
    else:
        print("ジョーク:", data['setup'])
        print("オチ:", data['delivery'])
else:
    print("API呼び出しに失敗しました。")
