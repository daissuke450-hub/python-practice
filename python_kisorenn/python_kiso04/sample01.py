import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("猫の豆知識:", data['fact'])
else:
    print("API呼び出しに失敗しました。")
