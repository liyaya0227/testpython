#创建者：liyaya
#创建时间： 
print('-------------------面向对象------------------')
#类和对象
print('-------------------定义类------------------')
class Student:
    #定义在类中的变量，称为类属性
    native_place = '淮安'

    #初始化类方法
    def __init__(self, age, name):
        self.name = name #将局部变量name的值，赋值给实例属性
        self.age = age

    #静态函数
    @staticmethod
    def sm():
        print('这是静态函数，使用了staticmethod修饰')

    #类函数
    @classmethod
    def cm(cls):
        print('这是类函数，使用了classmethod修饰')

    # 在类里面的函数，称为实例方法
    def eat(self):
        print('这是实例方法')

#在类外定义的函数，成为函数
def sleep ():
    print('这是函数')

print('-------------------对象的创建------------------')
#对象的创建，叫类的实例化
#创建Student的实例对象
stu1 = Student('张三', 20)
stu1.eat()  #类对象.方法名，调用实例方法
print(stu1.name)
print(stu1.age)
Student.eat(stu1) #类名.方法名（类对象），调用实例方法和p37效果相同

print('-------------------类属性和类方法的调用------------------')
#类属性，被该类的所有对象所共有
stu2 = Student('李四', 30)
print(stu1.native_place)
print(stu2.native_place)
#静态方法、类方法，直接使用类名调用
Student.cm()
Student.sm()

print('-------------------动态绑定类属性和方法------------------')
class Student1:
    def __init__(self,name, age): #初始化函数里面的变量，可以被多次实例化
        self.name = name
        self.age = age
    def eat(self):
        print('学生吃饭饭')
stu3 = Student('pop', 20)
stu4 = Student('pipi', 30)
stu3.eat()
stu4.eat()
stu3.gender = '女' #为类对象动态绑定属性，只能该对象调用
print(stu3.gender)
def sleep():
    print('学生在睡觉觉')
stu4.sleep = sleep #为类对象动态绑定方法，只能该对象调用
stu4.sleep()