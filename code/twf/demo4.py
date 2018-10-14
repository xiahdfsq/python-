#unix时间戳，1970.1.1.0.0.0中秒数
#可以了解下AOP
import time

def decorator(func):
	def wrapper(*args, **kw):
		print(time.time())
		func(*args, **kw)
	return wrapper
@decorator
def f1(name):
	print('my name is'+name)
f1('justin biber')

@decorator
def f2(name, age):
	print('my name is '+name, 'now '+age)
f2('cindy', '26')

@decorator
def f3(name, age, ):
	print('my name is '+name, 'now '+age)
f3('cindy', '26',5,6,88)

#f = decorator(f1)
#f()