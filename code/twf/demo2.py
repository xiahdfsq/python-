
#reduce,第一个参数是连续计算的公式，list是连续带入的值，第三个是初始值

from functools import reduce 
list_x = [1,2,3,4,5,6,7,8]
f3 = reduce(lambda x,y: x+y, list_x, 10)
print(f3)
 