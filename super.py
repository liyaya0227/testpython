
#创建者：liyaya
#创建时间： 
print('-----------------python的封装、继承和多态------------------')
print('-----------------python的封装------------------')
#python中没有专门的修饰符，不允许外界访问类属性，但是可以使用两个_，定义之后的类属性，不允许外界访问
class Student:
    def __init__(self, name, __age):
        self.name = name
        self.__age = __age
    def show(self):
        print(self.__age)  #虽然被__修饰的类属性不能被外部访问，但是可以通过实例方法进行访问
stu1 = Student('张三', 20)
stu1.show()
print(stu1.name)
print(stu1._Student__age)  #虽然被__修饰的类属性不能被外部访问，但是还可以通过：_类名__类属性名来访问（不建议使用）

print('-----------------python的继承------------------')
#继承的语法： class 子类 （父类1，父类2，父类3，....）：  支持多继承
#                     pass
#如果一个类没有继承父类，默认继承object类
#定义子类时，必须在构造函数中调用父类的构造函数
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)
class Student1 (person):
    def __init__(self, name, age, no):
        super().__init__(name, age)  #用super().调用父类的构造函数
        self.no = no
    def info(self):     #如果子类对继承的父类的某些属性或者方法不满意时，可以在子类中对其（方法体）重写
        super().info()  #子类重写其方法体之后，可以使用super().XXX，调用父类中被重写的方法
        print(self.no)

    def __str__(self):    #重写_str_方法
        return f'我的名字是{self.name},我今年{self.age}岁'
class Teacher(person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)  #用super().调用父类的构造函数
        self.gender = gender
stu2 = Student1('张三', 20, '1001')
stu2.info()
teacher = Teacher('李老师', 30, '女')
teacher.info()

print('-----------------python的方法重写------------------')
#如果子类对继承的父类的某些属性或者方法不满意时，可以在子类中对其（方法体）重写
#子类重写其方法体之后，可以使用super().XXX，调用父类中被重写的方法

print('-----------------object类------------------')
#object类是所有类的父类，我们可以调用它的全部属性和方法
#内置函数dir()可以查看指定对象的所有属性
#object有一个内置函数_str_()方法，用于返回对一个对于’对象的描述‘，对应于内置函数str()经常用于print()方法
#帮助我们查看对象的信息，所以我么经常对_str_()方法重写
print(dir(stu2))
print(str(stu2))  #默认返回内存地址值，重写后会被替换


print('-----------------python的多态------------------')
#python是动态语言，不需要关心对象是什么类型的，只需要关心对象的行为
class Aminal():
    def eat(self):
        print('动物要吃东西的。。。。')
class Dog(Aminal):
    def eat(self):
        print('狗狗吃骨头。。。')
class Cat(Aminal):
    def eat(self):
        print('猫猫吃鱼。。。')
class Person():
    def eat(self):
        print('人吃大米饭哦。。。')
def fun(obj):   #只要该对象有eat()这个方法，那么就可以作为参数
    obj.eat()
fun(Dog())
fun(Cat())
fun(Aminal())
fun(Person())

print('-----------------python的特殊属性------------------')
class A:
    pass
class B:
    pass
class C(A,B):
    pass
c = C()
#实例对象的属性字典
print(c.__dir__)
print(C.__dir__)
#输出对象所属的类
print(c.__class__)
print(C.__class__)
#输出类的父类元素
print(C.__bases__)
print(C.__base__)
#输出类的层次结构
print(C.__mro__)

print('-----------------python的特殊方法------------------')
#__dict__:获得类对象或者实例对象的所有属性和方法的字典
#__add__:通过重写__add__方法，可使用自定义对象具有“+”的功能
a = 10
b = 20
#c = a+b
c = a.__add__(b)
print(c)
class Test:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return len(self.name)
st1 = Test('张三')
st2 = Test('李四')
st3 = st1 + st2
print(st3)
#__len__:通过重写__len__方法，可以使内置函数len()的参数为自定义
lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())
print(st1.__len__())
#__new__:创建对象
#__init__:对创建的对象进行初始化