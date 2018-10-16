def out():
	a = 10

	def inner(x):
		return a * x * x

	return inner

f = out()
f(5)
f.__closure__



x=0
def walk(pos):
	def steStep(s):
		nonlocal pos
		pos = pos + s
		return pos


f = walk(x)
f.__closure__[0].cell.__contents

'''
flist = []
for i in range(3):
	def foo(x): print(x)
	flist.append(foo)	



#改进写法	
for i in range(3):
	def foo(x, y = i): print(x + y)
	flist.append(foo)


for f in flist
	f(2)

'''