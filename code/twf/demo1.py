#第12章 函数式编程： 匿名函数、高阶函数、装饰器
#python map函数

# for x in list_x:
# 	square(x)
	
list_x = [1,2,3,4,5,6,7,8]


def square(x):
	return x * x

f = map(square, list_x)
#函数式编程map,reduce,filter,lambda. 其本质还是 命令式编程；只是一个语法糖提供给你用
#匿名函数写法
f = map(lambda x: x*x, list_x)
print(list(f))

list_y = [1,2,3,4,5,6,7,8]

f2 = map(lambda x, y: x*x + y, list_x, list_y)

print(list(f2))




