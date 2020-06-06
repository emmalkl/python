#参数
''' 
1.必须参数
形式参数，实际参数 
2.关键字参数形式如下
为了代码的可读性！
def add(x,y):
    result=x+y
    return result
c=add(y=1,x=2)
3.默认参数
如果参数过长但要传递：（首先不要设计过长；或者使用对象）

'''
def add(x,y):
    result=x+y
    return result
c=add(y=1,x=2)

# c=add(x=2)#如果缺少必须参数，会报错


