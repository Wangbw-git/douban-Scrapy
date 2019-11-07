#quote函数：屏蔽特殊字符
import os,urllib
from urllib import parse
#对str进行编码
stra = parse.quote("this is python!")
print(stra)
#对str解码
print(parse.unquote(stra))
#使用'+'代替了%20和urllib.aprse.quote类似
strb = parse.quote_plus('this is python')
print(strb)
#解码
print(parse.unquote_plus(strb))

dicta = {'name':'zeping','password':'123456'}
#urlencode将字典转换为url参数
print(parse.urlencode(dicta))

#本地路径转换为url路径
# filename = parse.pathname2url('')

#功能：将单个字符串编码转化为 %xx 的形式
from urllib.parse import quote
"""特殊符号：汉字、&、=等特殊符号编码为%xx """
KEYWORD = '苹果'
url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
# keyword = quote(KEYWORD)
# print(keyword)
# keyword = parse.unquote(keyword)
# print(keyword)
print(url)
#运行结果：https://s.taobao.com/search?q=%E8%8B%B9%E6%9E%9C
KEYWORD = '='
url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
print(url)
#运行结果：https://s.taobao.com/search?q=%3D

"""url标准符号：数字字母 """
KEYWORD = 'ipad'
url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
print(url)
#运行结果：https://s.taobao.com/search?q=ipad
KEYWORD = '3346778'
url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
print(url)