from demo3 import Human

class Student(Human): 
	def __init__(self, school, name, age):
		super(Student, self).__init__(name, age)
		self.school = school 

	def doHomework(self):
		super(Student, self).doHomework()
		print('english')

 
		
student1 = Student('yizhong', 'jj', 22)
print(student1.__dict__)
