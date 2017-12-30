import requests
#尝试搜索
kv = {'wd':'Python'}
r = requests.get("http://www.baidu.com/s",params=kv)
print(r.status_code)
print(r.request.url)
