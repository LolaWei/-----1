class Sys():
    def __init__(self):
        self.students = {}    #定义一个空字典以存储学生信息
    def menu(self):           #菜单列表
        print("=======================")
        print("欢迎进入学生信息管理系统!")
        print("按1添加学生信息")
        print("按2查询学生信息")
        print("按3删除学生信息")
        print("按#退出系统")

    def add_info(self):          #添加信息
        print("您选择了添加学生信息功能！")
        new_name=input("请输入学生姓名：")
        new_number=input("请输入学生学号：")
        new_age=input("请输入学生年龄：")
        new_score=input("请输入学生成绩：")
        self.students[new_number]=(new_name,new_age,new_score)
        print(self.students.keys())
        print("信息已保存成功！")

    def get_info(self):          #获得学生信息
        print("您选择了获取学生信息的功能！")
        num=input("请输入学生学号：")
        if num in self.students.keys():
            print("name:",self.students[num][0]+"\n" "age：",self.students[num][1]+"\n" "score：",self.students[num][2])
        else:
            print("该学生不存在！")

    def del_info(self):            #删除学生信息
        print("您选择了删除学生信息功能！")
        num=input("请输入学生学号：")
        if num in self.students.keys():
            del self.students[num]
            print("信息已成功删除！")
        else:
            print("该学生不存在！")

    def exit_sys(self):           #退出系统
        print("您已成功退出系统！")

def main():
    sys = Sys()
    while True:
        sys.menu()            #显示菜单
        key=input("请输入您的选择：")
        if key=="1":
            sys.add_info()
        elif key=="2":
            sys.get_info()
        elif key=="3":
            sys.del_info()
        else:
            sys.exit_sys()
            break

if __name__=="__main__":
    main()






