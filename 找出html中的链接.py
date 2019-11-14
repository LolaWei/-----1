from bs4 import BeautifulSoup as bs
def find_links(filename):
    soup=bs(open(filename,encoding="utf-8"),"html.parser")
    urls=soup.find_all("a")
    for u in urls:
        print(u["href"])
    content=soup.get_text().strip("\n")
    print(content)


if __name__=="__main__":
    find_links(r"C:\Users\hp\Desktop\Python爬虫利器二之Beautiful Soup的用法 _ 静觅.html")


