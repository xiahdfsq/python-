#Python的高级语法与用法.
#枚举 可以防止变更
#枚举 可以防止标签key相同
from enum import Enum

class VIP(Enum):
	YELLOW = 1
	GREEN = 2 

print(VIP.YELLOW)
print(VIP.YELLOW.value)
print(VIP.YELLOW.name)