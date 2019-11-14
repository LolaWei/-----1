from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup=BeautifulSoup(html,"html.parser")
#print (soup.prettify())
print(soup.title)
print(soup.head)
print (soup.a) #查询的是第一个符合的标签
print(soup.p)
print(type(soup.a))
#对于tag，它有两个重要的属性，name和attrs
print(soup.name)     #对于soup来说，name是【document】
print(soup.head.name)   #对于标签来说，name就是标签本身的名字
#attrs
print(soup.p.attrs)    #得到的结果会把它的属性列出来，并以字典的形式呈现出来
soup.p.attrs["class"]="newclass" #可以对其属性进行修改
del soup.p.attrs["class"]   #可以删除这个属性

#获取标签内部的文字，用.string
print(soup.p.string)
print(type(soup.p.string))   #这是一个navigableString

#以下介绍遍历文档树
print(soup.head.contents)  #将tag的子节点以列表形式输出
print(soup.head.children)   #它返回的不是list，但是我们可以通过遍历获取所有的子节点
print(soup.descendants)   #contents 和children仅包含tag的直接子节点，而descendants包含所有的节点
for child in soup.descendants:
    print (child)

#获取多个内容
for string in soup.strings:
    print(repr(string))
#去除多余的空格或空行
for string in soup.stripped_strings:
    print(repr(string))
#还有父节点与兄弟节点等
#find_all方法  find_all( name , attrs , recursive , text , **kwargs )
print(soup.find_all("a"))  #最后以列表的形式呈现
#也可以使用soup.select()来查找标签
print(soup.select("a"))


