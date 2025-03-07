#直接在控制台输出
print("hello world")

#在文件中输出信息
fp=open("D:/testpy/a.text","a+")#a的意思是，如果没有文件就创建，有了就在已有内容后面追加
print("hello world",file=fp)
fp.close()

#输出的内容不换行，用逗号分隔
print('hello','world','python')