# import requests, json

# r = requests.get("https://v6.exchangerate-api.com/v6/ea6ef78e98f0b9230fccc229/latest/KRW")
# dt_dict = r.json()
# print(dt_dict['conversion_rates'])

# import requests, json, time

# for _ in range (5):
#     r = requests.get("http://api.open-notify.org/iss-now.json")
#     r_dict = r.json()
#     print(r_dict["iss_position"])
#     time.sleep(5)

# import requests, json

# url="https://v6.exchangerate-api.com/v6/7a91e6d981f56e6bb66304ca/latest/USD"
# r=requests.get(url)
# dt_dict=r.json()
# print(dt_dict['conversion_rates']['KRW'])

import requests, json, pandas as pd
url="https://v6.exchangerate-api.com/v6/7a91e6d981f56e6bb66304ca/latest/USD"
r=requests.get(url)
dt_dict=r.json()
print(pd.DataFrame.from_dict(dt_dict['conversion_rates'], orient='index'))