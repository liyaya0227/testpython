#创建者：liyaya
#创建时间： 
print('-------------------字符串--------------------')
#字符串的驻留机制：不同的变量存储相同的字符串，只对应同一个内存地址：
#前提：字符串的长度为0-1
#字符串符合标识符
#只在编译时驻留，而非运行时
#[-5，256]之间的整数数字

#驻留机制的好处：节约内存，提升效率
#拼接字符串，建议使用jion()而不是使用+号

print('-------------------字符串的常用操作--------------------')
'''字符串的查询操作'''
#index(): 正向索引，查找字符串第一次出现的位置，如果未查询到，抛出异常ValueError
str1 = 'hello,mylove'
print(str1.index('lo'))
#rindex()： 反向索引，查找字符串第一次出现的位置,如果未查询到，抛出异常ValueError
print(str1.rindex('lo'))
#find()：正向索引，查找字符串第一次出现的位置,如果未查询到，返回-1
print(str1.find('lo'))
print(str1.find('lol'))
#rfind()： 反向索引，查找字符串第一次出现的位置,如果未查询到，返回-1
print(str1.rfind('lo'))
print(str1.rfind('lol'))

'''字符串的大小写转换'''
#upper(): 将字符串全都转成大写，并开辟新的内存地址
str2 = 'do u wanna happy ? jion US'
print(str2.upper())
#lower()： 将字符串全都转换成小写，并开辟新的内存地址
print(str2.lower())
#swapcase()： 将字符串中，所有的大写字母转成小写，所有的小写字母转成大写
print(str2.swapcase())
#capitalize()： 将字符串的第一个字母转成大写，其他都转成小写字母
print(str2.capitalize())
#title()：将字符串中的每个单词的首字母转成大写，其余转成小写
print(str2.title())

'''字符串内容的对齐操作'''
#居中对齐：center():有两个参数，第二个参数可以省略，第一个参数指定宽度，如果长度大于字符串长度，居中显示
#左右由第二个参数指定的样式展示，默认为空；如果长度小于字符串长度，显示原字符串
str3 = 'what is your meaning for'
print(str3.center(30, '#'))
print(str3.center(30))
print(str3.center(10))
#左对齐：ljust(): 有两个参数，第二个参数可以省略，第一个参数指定宽度，如果长度大于字符串长度，靠左显示
#右边由第二个参数指定的样式展示，默认为空；如果长度小于字符串长度，显示原字符串
print(str3.ljust(30, '#'))
print(str3.ljust(30))
print(str3.ljust(10))
#右对齐：rjust(): 有两个参数，第二个参数可以省略，第一个参数指定宽度，如果长度大于字符串长度，靠右显示
#左边由第二个参数指定的样式展示，默认为空；如果长度小于字符串长度，显示原字符串
print(str3.rjust(30, '#'))
print(str3.rjust(30))
print(str3.rjust(10))
#右对齐：zfill(): 只有一个参数指定宽度，左边用0填充，如果长度大于字符串长度，靠右显示
#左边由第二个参数指定的样式展示，默认为空；如果长度小于字符串长度，显示原字符串
print(str3.zfill(30))
print(str3.zfill(10))

'''字符串的分割'''
#split():  默认分割符是空格，返回一个列表
#可以指定参数sep(): 设置分割符
#可以指定参数maxsplit(): 设置最大分割次数，剩余的字符串，会以一个整体返回列表
print(str3.split())
str4 = 'what| is | meaning | for'
print(str4.split(sep='|', maxsplit=2))
#rsplit():  反向分隔符，默认分割符是空格，返回一个列表
#可以指定参数sep(): 设置分割符
#可以指定参数maxsplit(): 设置最大分割次数，剩余的字符串，会以一个整体返回列表
print(str3.rsplit())
str4 = 'what| is | meaning | for'
print(str4.rsplit(sep='|', maxsplit=2))

'''字符串判断的相关方法'''
# isidentifier()：判断字符串是不是合法的字符串
print('hello,mylove'.isidentifier())
print('hello123'.isidentifier())
# isspace(): 判断字符串是不是全部都由空白字符组成（回车、换行、水平制表符）
print('\t'.isspace())
print('\r'.isspace())
print('\n'.isspace())
# isalpha() : 判断字符串是否都由字母组成
print('hello123'.isalpha())
print('hello张三'.isalpha())
# isdecimal() : 判断字符串是否都由十进制数字组成
print('123Ⅰ'.isdecimal())
print('123'.isdecimal())
# isnumeric(): 判断字符串是否都有数字组成
print('123'.isnumeric())
print('123Ⅰ'.isnumeric())
# isalnum(): 判断字符串是否都由数字和字母组成
print('123hello'.isalnum())
print('123hello张三'.isalnum())

'''字符串的替换和合并'''
#替换： replace(): 可以有三个参数，第一个参数指定原字符串中要替换的字符串，第二个参数指定要替换后的字符串，第三个参数，指定最大替换次数
str5 = 'hello,love,love,mylover,1111,1111,1111'
print(str5.replace('love', 'python'))
print(str5.replace('1111', 'python', 1))
#合并： jion(): 列表或元组中的字符串合并成一个字符串，字符串可以合并
print('*'.join(str5))
lst = ['do', 'u', 'wanna', 'my', 'love']
print('|'.join(lst))
print(''.join(lst))
t1 = ('goodbye', 'beauty', 'hello', 'beast')
print(''.join(t1))

'''字符串的比较操作'''
#可以使用 >、<、>=、<=、==、!=等对字符串进行比较，比较的是value是否相同
#可以使用内置函数ord()，查看字符串的原始值//参数类型为character
#或者使用chr()，查看字符串的编码值//参数类型为int
a = b = 'pyhton'
print(a > b)
print(a == b)
print(ord('a'), ord('b'))
print(chr(45621))
print(ord('杨'), ord('花'))

'''字符串的切片操作'''
#[start:stop: step]
str6 = 'hello,python'
print(str6[:5])
print(str6[6:])
str7 = '!'
print(str6[:5] + str7 +str6[6:])
print(str6[::2])
print(str6[::-1])

'''格式化字符串'''
#第一种方法，使用%作为占位符，%s,%d,%f，实际值用元组显示%（value,value,...）
name = 'leyaya'
age = 25
print('我叫%s,我今年%d岁'% (name, age))
#第二种方式，使用{0,1,2,.....}作为占位符，实际值用format()函数.format(argument,argument,.....)
print('我叫{0}，我今年{1}岁，{0}最好看了'.format(name, age))
#第三种方式，直接使用f-string, f{value}
print(f'我叫{name},我今年{age}岁')
#设置宽度和精度：宽度：占位符前加数字；精度：.3f
pi = 3.1415926
print('%10.3f'%(pi))
print('{0:20.3f}'.format(pi))#冒号左边的0:代表第几个参数；冒号右边表示设置的宽度和精度

'''字符串的编码和解码'''
#编码和解码的格式要相同
#编码：encode
#解码：decode
str8 = '天涯共此时'
print(str8.encode(encoding='GBK'))
print(str8.encode(encoding='UTF-8'))

byte = str8.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))