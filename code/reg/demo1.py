import re

str_var = 'abc,c#\n agc,afc'

str1 = re.findall('a[^df]c', str_var, re.I | re.S)



str_var2 = ' pythonC#javaC#PHP'

def convert(value):
	return '!!'+value.group()+'!!'

str2 = re.sub('C#', convert, str_var2, 1)

#match 第一个字母开始匹配， 不合格就返回None
##search 一旦成功就匹配，非贪婪模式


str_var3 = 'life is short, i use python, i love python'

str4 =re.match('life(.*)python', str_var3)
print(str4.span())

str5 = re.search('life(.*)python(.*)python', str_var3)
str5.group(1)
str5.group(0,1,2)
