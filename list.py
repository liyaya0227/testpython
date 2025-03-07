#创建者：liyaya
#创建时间： 
#列表的增删改
print('------------------------列表的添加-------------------------')
#列表的添加
#append()
lst = ['hello', 'my', 'love', 'long', 'time', 'no', 'see', 999.9]
lst2 = list([10, 20, 30])
lst.append(00)
print(lst)
print(lst2)
#extend()
lst.extend([lst2])
print(lst)
lst.extend(lst2)
print(lst)
#insert()
lst.insert(2,'bye')
print(lst)
#切片操作
lst[4:] = lst2
print(lst)

print('------------------------列表的删除-------------------------')
#列表的删除
#remove()：一次删除一个元素，如果有重复的元素，则删除第一个元素
lst3 = [10, 20, 30, 30, 30, 40, 50, 60]
lst3.remove(30)
print(lst3)

#pop()：删除指定位置的元素；如果为空的话，默认删除数组的最后一个元素
lst3.pop(3)
print(lst3)
lst3.pop()
print(lst3)

#切片操作：截取列表的元素
#要想删除列表的某段元素，要对切片的元素，赋值为空数组
new_list = lst3[1:3]
print(new_list)

lst3[1:3] = []
print(lst3)

#clear()，清空列表元素
lst3.clear()
print(lst3)
#del,删除表结构
'''del lst3
print(lst3)'''

print('------------------------列表的修改-------------------------')
#列表修改元素
lst4 = [10, 20, 30, 40]
lst4[2] = (100)
print(lst4)
#用切片操作修改元素：切片的内容用新的数组替换
lst4[1:3] = ['hello', 'my', 'darling']
print(lst4)

print('------------------------列表的排序-------------------------')
#使用sort()，列表元素升序排列；加参数reverse = True，列表元素降序排列：该排序是在原列表上进行排序
lst5 = [10, 60, 30, 44, 56]
lst5.sort()
print(lst5)
lst5.sort(reverse = True)
print(lst5,id(lst5))
#使用sorted()函数，进行排序，是将原列表的元素排序后赋值到新的列表中
lst6 = sorted(lst5)
print(lst6,id(lst6))
