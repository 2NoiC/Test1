import requests

domain = "https://api.vk.com/method"
access_token = '644c6f1ee15c472b37b3a0f41bfeccc3fdd3d9ea3f371f46aa9e838a9062aeeb4c6b5d662faef4930ecbf'
user_id = '157844385'
fields = 'sex'
v = '5.124'

query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
response = requests.get(query)
print(response.text)