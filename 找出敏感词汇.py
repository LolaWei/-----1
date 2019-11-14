def replace_words(temp):
    l=[]
    with open(r"C:\Users\hp\Desktop\filtered_words..txt") as f:
        for each in f.readlines():
            l.append(each.strip())
        for i in l:
            if i in temp:
                print(temp.replace(i,"**"))

def main():
    temp=input("请输入：")
    replace_words(temp.strip())

if __name__=="__main__":
    main()
