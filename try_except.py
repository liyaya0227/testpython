#创建者：liyaya
#创建时间： 
print('--------------------try  except-------------------')
try:
    a = int(input('请输入一个被除数：'))
    b = int(input('请输入一个除数：'))
    c = a/b
    print(c)
except ValueError :
    print('只能输入整数')
except ZeroDivisionError:
    print('除数不能为0哦')

print('--------------------try  except  else-------------------')
try:
    a = int(input('请输入一个被除数：'))
    b = int(input('请输入一个除数：'))
    c = a/b
except BaseException as e :
    print('出错了哦', e)
else:
    print(c)

print('--------------------try  except  else   finally(一定会执行的代码块：通常是释放内存)-------------------')
try:
    a = int(input('请输入一个被除数：'))
    b = int(input('请输入一个除数：'))
    c = a/b
except BaseException as e :
    print('出错了哦', e)
else:
    print(c)
finally:
    print('谢谢您的使用')

print('--------------------python中常见的异常类-------------------')
#ZerodivisionError: 除（或取模）零（所有数据类型）
#IndexError: 序列中没有此索引（index）
#KeyError: 映射中没有这个键（key）
#NameError: 未声明/初始化对象（没有属性）
#SyntaxError: python 语法错误
#ValueError: 传参无效

print('--------------------trackback模块-------------------')
import traceback
try:
    print('-------------')
    print(1/0)
except:
    traceback.print_exc()  #打印异常