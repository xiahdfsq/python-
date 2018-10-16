#引入模块的方式


# import demo1
# a = demo1.A

# import demo1 as out
# a = out.A

# from demo1  import A
# a = A

#引入t包下面的模块

# from t import child
# a = child.PI

# from t.child import PI
# a = PI

#这个时候I不可以导入
# from t.child import *
# a = R

#换行导入 这个时候I可以导入
# from t.child import (PI, R,
# I)
# a = I

from t import *

a = child.I
#报错
#b = child2.e
print(a)

