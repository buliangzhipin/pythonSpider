import requests
#Referer=pixiv 防盗链
kv = {'Referer':"https://www.pixiv.net/"}#Referer=“http://www.pixiv.net/”
path = "D:/test/test.jpg"
url="https://i.pximg.net/img-original/img/2017/12/29/00/48/02/66511081_p1.jpg"
r = requests.get(url,headers=kv)
print(r.status_code)
print(r.request.headers)

with open(path,'wb') as f:
    f.write(r.content)

'''
标准写法
import requests
import os
url =""
root = ""
split把最后一个/提取出来
path = root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f
            f.write(r.content)
            f.close()
            print("成功保存")
    else:
        print("文件已存在")
except:
    print("读取失败")
'''