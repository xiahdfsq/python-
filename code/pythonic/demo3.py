#None 空 不等于 空字符串 空列表 0 False

a = ''
b = False
c = []
x = None
print(x == a)
print(x == b)
print(x == c)

print(a is None)
print(type(None)) #NoneType

def fun():
	return None

x = fun()
#a = []
#判空
if not x:
	print('s')

