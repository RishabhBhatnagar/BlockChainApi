import requests
data = dict(file_name='as', sender_name='as', receiver_name='as', file_size='asd')
url = "http://127.0.0.3:5000/see_blockchain"
r = requests.post(url=url, data=data)

result = []
for dictionary in eval(r.text):
    itemset = []
    for key, value in dictionary.items():
        itemset.append("<b>{}</b>: {}".format(key, value))
    result.append("<br>".join(itemset))


with open('del.html', 'w') as f:
    f.write("<hr>".join(result))

