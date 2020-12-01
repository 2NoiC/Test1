import requests

domain = "https://api.vk.com/method"
access_token = 'your token'
user_id = '157844385'
fields = 'sex'
v = '5.124'

query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
response = requests.get(query)
print(response.text)