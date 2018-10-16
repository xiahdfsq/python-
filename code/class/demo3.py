class Human(): 
	sum1 = 0
	def __init__(self, name, age): 
		self.name = name
		self.age = age

	def getName(self):
		return self.name
		
	def doHomework(self):
		print('math')