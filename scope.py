#创建者：liyaya
#创建时间：
print('-------------------参数的作用域--------------------')
def fun(a, b):
    global c
    c = a + b
    print(c)
fun(1, 2)
print(c)
'''在局部变量前添加关键字global ，可以将其作用域更改为全局'''


print('-------------------递归函数--------------------')
def fun1(n):
    if n == 1:
        return  1
    else:
        return  n * fun1(n-1)
print(fun1(6))

print('-------------------斐波那契函数--------------------')
def fun2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fun2(n-1) + fun2(n-2)
print(fun2(6))

for i in range(1,7):
    print(fun2(i))