#创建者：liyaya
#创建时间：
print('---------------bug------------------')
#查找某个演员是否在列表中
lst = [{'rating': [9.6, 90766], 'id': 2765362, 'type':['剧情', '犯罪'], 'title':'肖申克的救赎', 'actors': ['提姆.罗宾斯', '摩根.佛力曼']},
       {'rating': [9.5, 90416], 'id': 2741362, 'type':['剧情','同性', '爱情'], 'title':'霸王别姬', 'actors': ['张国荣', '巩俐', '张丰毅', '葛优']},
       {'rating': [9.7, 94466], 'id': 1465362, 'type':['剧情', '爱情'], 'title':'阿甘正传', 'actors': ['汤姆.克鲁斯', '罗宾.怀特']}]
def fun(name):
   for item in lst:
       '''print(item['actors'])'''
       for actor in item['actors']:
           if name in actor:
                print(name + '出演了'+ item['title'])

str = input('请输入你想要查询的演员名称：')
fun(str)