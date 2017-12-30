import requests
r =requests.get("https://python123.io/ws/demo.html")
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())
# soup = BeautifulSoup('<p>data</p>','html.parser')
# print(soup.prettify())
#title获取
print(soup.title)
#a标签获取 然后a父标签
print(soup.a.parent.name)
#内容
print(soup.a.attrs)
print(soup.a.attrs['class'])
#type
print(type(soup.a))
#p的内容
print(soup.p.string)

#遍历
print(soup.head.contents)
print(soup.body.contents)