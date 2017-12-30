import requests
payload = {'key1':'value1','key2':'value2'}#提交的字典
r = requests.post("http://httpin.org/post",data=payload)
print(r.text)