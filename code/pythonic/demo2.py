#集合推导式
#map

a = [1,2,3,4,5,6,7,8]

#列表推导式
b = [i**3 for i in a if i <= 4]
print(b)

students = {
	'细小当': 18,
	'细小当2': 13,
	'细小当3': 14,
}

#b2 = [key for key,value in students.items()]
#b2 = {value: key for key,value in students.items()}
b2 = (key for key,value in students.items())#得到generator,元组是不可遍历
for x in b:
	print(x)

print(b2)