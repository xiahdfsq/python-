#对象存在并不一定是True
#False : '',[],None
#__len__与__bool__

class Test():
	def __bool__(self):
		#只能返回布尔类型
		return False
	def __len__(self):
		#只能返回True 正整数 0
		return 1
		#return 0

test = Test()
if test:
	print('s')
else:
	print('f')

print(bool(Test()))

		