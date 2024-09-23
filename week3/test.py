import requests, json

r = requests.get("https://v6.exchangerate-api.com/v6/ea6ef78e98f0b9230fccc229/latest/KRW")
dt_dict = r.json()
print(dt_dict['conversion_rates'])