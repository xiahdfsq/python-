#对类调用


from demo1 import Student

student1 = Student('kk', 11)
student2 = Student('jj', 16)

a = student1.setScore(59)
Student.fn()

print(student1.__dict__)
#强制读取私有变量
print(student1.Student.__privatevar)