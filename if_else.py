#创建者：liyaya
#创建时间： 
#顺序结构

#选择结构
#语法结构  if  条件表达式 ：
#              条件执行体
# 例子1
money = 2000
s = int(input('请输入你的取款金额'))
if money > s :
    money = money - s
    print('您的余额还剩',money)
else :
    print('您的余额不足')

#例子2 多分支结构
score = int(input('请输入您的成绩:'))
if 90<=score<=100 :
    print('您的成绩为A')
elif 80<=score<=89 :
    print('您的成绩为B')
elif 70 <= score <= 79:
    print('您的成绩为C')
elif 60 <= score <= 69:
    print('您的成绩为D')
else:
    print('您的成绩无效')

#例子3 嵌套结构
vip = input('您是会员嘛？y/n')
money = float(input('您的消费金额为：'))
if vip == 'y':
    if money >200 :
        print('打8折，您的付款金额为：',money*0.8)
    elif money >100 :
        print('打9折，您的付款金额为：', money * 0.9)
    else:
        print('不打折，您的付款金额为：',money)
else:
    if money >300:
        print('打9折，您的付款金额为：',money*0.9)
    else:
        print('不打折，您的付款金额为：',money)


#循环结构