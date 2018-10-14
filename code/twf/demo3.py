#filter 过滤函数

list_x = [1,2,3,4,5,6,7,8]

#r = filter(lambda x: x>3, list_x)

r = filter(lambda x: True if x>3 else False, list_x)
print(list(r))
