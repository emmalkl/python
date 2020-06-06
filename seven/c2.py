#引入模块c1
import c1
#引入模块c3
import t.c3
#引入模块c4,简写
import t.c4 as m
#引入模块c5中的变量，解决命名空间过长的问题
from t.c5 import c
# from t import c5
#上面这行是引入c5 的模块
#引入模块c5中的所有变量；可以但不推荐
# from t.c5 import *

from t.c6 import *

print(c1.a)
print(t.c3.b)
print(m.a)
print(t.c5.c)
# print(d)
# print(e)
print(a)
print(c)
print(d)


