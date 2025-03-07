#创建者：liyaya
#创建时间： 
#创建者：liyaya
#创建时间：
import  os
filename = 'studentlist.txt'
def main():
    while True:
        menu()
        try:
            num = int(input('请输入您想操作的菜单编号：'))
            if num in [0, 1, 2, 3, 4, 5, 6, 7]:
                if num == 0:
                    choice = input('您确定要推出系统嘛？y/n')
                    if choice == 'y' or choice == 'Y':
                        break
                    else:
                        continue
                elif num == 1:
                    insert()
                elif num == 2:
                    search()
                elif num == 3:
                    delete()
                elif num == 4:
                    modify()
                elif num == 5:
                    sort()
                elif num == 6:
                    total()
                elif num == 7:
                    show()
            else:
                print('您输入的菜单编号不存在，请重新输入!')
        except ValueError:
            print('请输入正确的菜单编号！')


def menu():
    print('===================学生信息操作系统===================')
    print('------------------------功能菜单----------------------')
    print('\t\t\t\t1、录入学生信息')
    print('\t\t\t\t2、查找学生信息')
    print('\t\t\t\t3、删除学生信息')
    print('\t\t\t\t4、修改学生信息')
    print('\t\t\t\t5、排序')
    print('\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t0、退出系统')
    print('------------------------功能菜单----------------------')

def insert():
    student_list = []
    while True:
        id = input('请输入学生学号：')
        if not id:
            break
        name = input('请输入学生姓名：')
        if not name:
            break
        try:
            age = int(input('请输入学生年龄：'))
            english = int(input('请输入学生的英语成绩：'))
            python = int(input('请输入学生的python成绩：'))
        except ValueError:
            print('只能输入整数哦！')
            continue
        except UnboundLocalError:
            print('出错了！')
            continue
        dict = {'id': id, 'name': name, 'age': age, 'english': english, 'python': python}
        student_list.append(dict)
        #print(student_list)
        answer = input('是否继续添加学生信息？y/n'+'\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    #将字典中的内容保存到文件当中，以字符串的形式保存
    #print(student_list)
    save(student_list)
    print('学生信息添加成功！')

#save()函数，进行存储
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def search():
    '''
     while True:
        info = input('请输入要查找的学生id或者学生姓名：')
        if not info:
            break
        exict = os.path.dirname(filename)
        if exict:
            stu_txt = open(filename, 'r', encoding='utf-8')
            stu_txt.readlines()
            for stu in dict(eval(stu_txt)):
                if info in stu:
    '''

def delete():
    while True:
        student_id = input('请输入你想删除的学生学号：')
        if student_id != '':
            exist = os.path.exists(filename)
            if exist:
                with open(filename, 'r', encoding='utf-8') as file:
                    #将文件中的数据逐条读取，读取的数据会存放在列表中[]，列表中的数据类型是str
                    student_old = file.readlines()
                    #print(type(student_old))
                    print(student_old)
                    #定义一个标记，来判断学生学号是否相同
                    flag = False
                    #判断列表中的数据是否为空
                    if student_old:
                        with open(filename, 'w', encoding='utf-8')as wfile:
                            d = {}
                            for item in student_old:
                                d = dict(eval(item))
                                if d['id'] != student_id:
                                    print(item)
                                    wfile.write(str(d)+'\n')
                                else:
                                    flag = True
                    else:
                        student_old = []
                    if flag:
                        print(f'您输入的学生学号为{student_id}的学生信息已被删除！')
                    else:
                        print(f'没有找到学生学号为{student_id}的学生信息！')
            else:
                print('没有学生信息')
                break
        else:
            print('请正确输入学生学号！')
            break
        show()  # 删完之后重新显示所有学生信息
        # 判断是否继续删除
        answer = input('是否继续删除学生信息？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break



def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__ == '__main__':
    main()