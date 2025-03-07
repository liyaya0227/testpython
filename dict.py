#创建者：liyaya
#创建时间： 
#字典，字典以键值对形式存储，是可变序列，无序排列
# scores = {key:value, key:value,.......}
#字典的创建方式，直接用{}号进行创建
scores = {'张三': 28, '李四': 30, '王五': 26}
print(scores)
#字典的创建方式二，用dict()函数进行创建
student = dict(name='张三', age=25)
print(student)

#字典元素的操作
print('------------------------获取字典元素-----------------------')
#第一种直接使用[]号，参数为key，根据key查找出对应的值
print(scores['张三'])
#第二种是使用get()函数，获取对应的值
print(scores.get('张三'))
#使用函数和[]的区别在于，直接使用[]号如果查出的值为空，会报错；
# 而使用函数，如果查找的值不存在，会返回None，如果在方法里设置默认参数，那么如果未找到值，则返回默认参数
print(scores['王五'])
'''print(scores['小六'])'''
print(scores.get('王五'))
print(student.get('王五'))
print('------------------------字典元素的增删改操作-----------------------')
#判断元素是否在字典中
print('张三' in scores)  # 用key的值在字典中查找
print(30 in scores)
print('张三' not in scores)
#在字典中添加元素
scores['妹妹'] = 18
print(scores)
#修改字典中的元素
scores['妹妹'] = 20
print(scores)
#删除字典中的元素
del scores['张三']
print(scores)
#清空字典的元素
'''scores.clear()
print(scores)'''
print('------------------------获取字典的视图-----------------------')
#有三个函数，分别获取字典的key,value,和key-value对：keys(),values(),items()
#keys()
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))
#values()
values = scores.values()
print(values)
print(type(values))
print(list(values))
#items()
items = scores.items()
print(items)
print(type(items))
print(list(items)) #会把键值对，作为元组，存放在列表中

print('------------------------字典的遍历-----------------------')
#for 变量 in 字典 ：
for item in scores:
    print(item, scores[item], scores.get(item))

print('------------------------字典生成式-----------------------')
#使用zip()函数，对key-value进行打包操作，赋值给字典
#格式：参数 =  { key:value  for key,value in zip(keys,values)}
items = ['fruits', 'vegetables', 'milk']
prices = [20, 30, 40]
d = {item.upper():price for item,price in zip(items,prices)}
print(d)