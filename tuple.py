'''目前所知的可变序列有：列表、字典''' #操作内存地址不发生改变
lst = [10,20,30]
print(id(lst))
lst.append(40)
print(id(lst))

'''目前所知的不可变序列有：字符串、元组'''#操作内存地址发生改变
str = 'hello'
print(id(str))
str = str + 'love'
print(id(str))

print('-------------------元组的创建--------------------')
'''第一种创建方式：直接使用（）,元素用逗号隔开'''
t = ('hello', 'my', 'love', 99.9)
print(t)
print(type(t))
'''第二种创建方式，使用内置函数tuple（）,创建后将其赋值给变量'''
t1 = tuple(('good', 'bye', 'darling', 33))
print(t1)
print(type(t1))
'''注意：如果元组中只有一个参数，要在参数后使用一个逗号'''
t2 = 'python'
print(type(t2))
t3 = ('python',)
print(type(t3))

print('-------------------为什么元组是不可变序列--------------------')
'''注意事项: 1、元组中存储的是对象的引用；2、如果元组中的对象是不可变对象，那么不能再引用其他对象
3、如果元组中的对象是可变对象，那么允许它修改数据'''
t4 = (10, [20,30], 40)
print(type(t4[0]), id(t4[0]))
print(type(t4[1]), id(t4[1]))
print(type(t4[2]), id(t4[2]))
'''t4[1] = 100'''#不允许修改可变对象的引用
t4[1].append(100) #允许修改可变对象的数据
print(t4)

print('-------------------元组的遍历--------------------')
#如果知道元组的个数，可以直接使用下标进行输出
#通常使用for-in遍历元组
t5 = ('hello', 'python', 998)
print(t5[0])
print(t5[1])
print(t5[2])
for item in t5:
    print(item)



