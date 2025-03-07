#创建者：liyaya
#创建时间： 
print('-------------------集合--------------------')
#定义集合 set = {key1,key2,.....}
#创建集合的方式一，直接使用花括号{}
'''集合是无序排列，且不允许有重复元素，和字典一样：key值不允许重复'''
s = {10, 20, 30, 30, 40, 50, 60, 60}
print(set, type(set))
#创建集合的第二种方式，使用内置函数set()，可以将不同类型的数据转换成集合：可遍历数据、列表、字典、集合、字符串或者创建空集合
s1 = set(range(8))
print(s1, type(s1))
s2 = set([10, 20, 30, 30, 40])
print(s2, type(s2))
s3 = set({'张三':28, '李四':30})
print(s3, type(s3))
s4 = set('hello')
print(s4, type(s4))
s5 = set({10,20,30,50,60,60})
print(s5, type(s5))
#空集合，不能单独使用{}：这是空字典，只能使用set()
s6 = set()
print(s6, type(s6))

print('-------------------集合的相关操作--------------------')
#判断元素是否存在集合当中： in ；not in
s7 = {'hello', 'my', 'love', 22, 33, 44, 555}
print(22 in s7)
print(444 not in s7)
print('heal' in s7)
#向集合中添加元素
#每次在集合中添加一个元素：add()
s7.add('darling')
print(s7)
#每次在集合中添加多个元素：update()：可以添加多种类型：集合、数组、元组
s7.update({99, 77, 'good'})
s7.update(['beautiful', 1000])
s7.update(('are', 'u', 'ok'))
print(s7)

#集合元素的删除操作：
#remove(): 每次删除一个指定元素，如果指定元素不存在，报错
s7.remove(77)
print(s7)
# s7.remove(888): 不存在，报错
#discard(): 每次删除一个指定元素，如果指定元素不存在，不报错
s7.discard(99)
s7.discard('wahoo')
print(s7)
#pop(): 每次删除一个任意元素，不能指定参数
s7.pop()
print(s7)
s7.pop()
print(s7)
#clear(): 清空集合
s7.clear()
print(s7)

print('-------------------集合之间的关系--------------------')
#集合是否相等：判断条件只要元素相同就好
ss1 = {10, 20, 30, 40, 50}
ss2 = {10, 20, 30, 40}
ss3 = {10, 30, 40}
print(ss1 == ss2)
#集合是否是另外一个集合的子集: issubset()
print(ss1.issubset(ss2))
print(ss2.issubset(ss1))
print(ss3.issubset(ss1))
#集合是否是另外一个集合的超集: issuperset()
print(ss1.issuperset(ss2))
print(ss2.issuperset(ss3))
print(ss1.issuperset(ss3))
#判断两个集合是否有交集: isdisjoint()
print(ss1.isdisjoint(ss2))

print('-------------------集合的数据操作--------------------')
#集合的数据操作有： 交集、并集、差集、对称差集
#交集： intersection() ,和&符号相同
sss1 = {10, 20, 30, 40, 50}
sss2 = {20, 30, 40, 60}
sss3 = {10, 20, 30}
print(sss1.intersection(sss2))
print(sss1 & sss2)

#并集 ： union() ，和符号 | 相同
print(sss1.union(sss2))
print(sss1 | sss2)

#差集：difference()，和符号-相同
print(sss2.difference(sss3))
print(sss2-sss3)

#对称差集 ：symmetric_difference(), 和符号^相同
print(sss2.symmetric_difference(sss3))
print(sss2^ sss3)

print('-------------------集合生成式--------------------')
#{i*i for i in range(x)}: 将花括号{}改为[]，就是列表生成式
setx = {i*i for i in range(10)}
print(setx,type(setx))
setx1 = [i*i for i in range(10)]
print(setx1,type(setx1))