import requests
data = dict(file_name='as', sender_name='as', receiver_name='as', file_size='asd')
url = "http://127.0.0.3:5000/insert_blockchain"
r = requests.post(url=url, data=data)
print(r.text)
