import requests


payload = {'key1': 'yonghoon', 'key2': 'ganzi'}
# Get
# urllib.request 와 다르게 엄청 쉽다. params = 로 넘겨주기만 하면 된다.
r = requests.get('http://httpbin.org/get', params=payload)
# 상태를 보거나 읽어올때... 진짜 쉽다. 이것만 써야지
print(r.status_code)
print(r.text)
print(r.json())

# Post
r = requests.post('http://httpbin.org/post', data=payload)
print(r.status_code)
print(r.text)
print(r.json())

# Put
r = requests.put('http://httpbin.org/put', data=payload)
print(r.status_code)
print(r.text)
print(r.json())

# Delete

r = requests.delete('http://httpbin.org/delete', data=payload)
print(r.status_code)
print(r.text)
print(r.json())