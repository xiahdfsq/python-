#类名建议用驼峰法制，类下面的函数称为方法
class Student():
	#定义实力变量
	sum1 = 0
	#定义私有变量 严格意义没有私有 可以强制获取
	__privatevar = 'this a private var'

	#构造函数，self代表实例对象
	def __init__(self, name, age): 
		self.name = name
		self.age = age
		self.score = 0
		print(self.sum1)
		print(self.__class__.sum1)

	def setScore(self, score):
		self.score = score
	
	#私有方法，外部调用会报错
	def __setScore(self, score):
		self.score = score

	#类方法
	@classmethod
	def plus_sum(cls):
		cls.sum1 +=1

	#静态方法一般少用，不能访问类的类变量
	@staticmethod
	def add(x,y):
		return x+y
