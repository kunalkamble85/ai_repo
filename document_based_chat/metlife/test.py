import json
import requests

url = "https://sandbox-api.acispeedpay.com/auth/v1/auth/token"
token = "7f8226ff-c653-42ea-b761-3da645b48203"
data_map = {"grant_type": "client_credentials","client_id": "sandbox-apichanneldemo",
            "client_secret":"1f71fd9c-e7a5-4e98-bf8e-bbbd302020b8"}
result = requests.post(url, data = data_map, headers = {'Content-type': 'application/x-www-form-urlencoded', "X-Auth-Key": ""+token})
# print(result)
# print(vars(result))
data = result.json()
print(data)