from enum import Enum
from enum import IntEnum, unique


class VIP(Enum):
	YEL = 1
	GREEN = 1
	RED = 3

class VIP2(Enum):
	YEL = 1
	GREEN = 2
	RED = 3

class VIP3(Enum):
	YEL = 1
	GREEN = 1
	RED = 3

print(VIP.YEL == VIP.GREEN)
print(VIP.YEL == VIP2.YEL)
print(VIP.YEL == 1)
print(VIP.YEL.value == 1)

@unique
class VIP4(IntEnum):
	YEL = 1
	GREEN = '2'
	RED = 3

for i in VIP2.__members__.items():
	print(i)