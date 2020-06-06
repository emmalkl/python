''' def funcname(parameter_list):
    pass '''



# 编写一个函数实现两个数字相加
def add(x,y):
    return x+y

# 打印输入参数
def printf(code):
    print(code)
    return
    print(code)
    print(code)
    print(code)#后面这3个打印不会执行


#调用函数
a=add(1,2)
b=printf(10)#printf内部是没有return的，所以b没有值返回Nnne
print(a,b)
''' 结果是：10
3 None '''

