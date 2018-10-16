#序列解包

a,b,c = 1,2,3
e=k=g=1


def fn(a1,a2,a3=33,*a4):
	print(a3)
	print(a4)

fn(1,2,3,4,5,6)


def fn2(a1,a2):
	print(a1)
	print(a2)

fn(a2=1,a1=2)