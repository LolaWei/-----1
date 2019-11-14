import os
import requests
from bs4 import BeautifulSoup as bs
url="http://tieba.baidu.com/p/2166231880"
data=requests.get(url)  #data是一个对象
soup=bs(data.text,"html.parser")
img_urls=soup.find_all("img",bdwater="杉本有美吧,1280,860")
for url in img_urls:
    print(url)


