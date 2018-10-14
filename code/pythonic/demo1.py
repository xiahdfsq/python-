#用字典来代替其他语言的switch语句
def get_sunday():
	return 'sunday'

def get_monday():
	return 'sunday'

def get_tuesday():
	return 'sunday'

def get_default():
	return 'unkown'

switcher = {
	0: get_sunday,
	1: get_sunday,
	2: get_sunday
}

day = 4
#day_name = switcher[day]
day_name = switcher.get(day, get_default)()
print(day_name)


