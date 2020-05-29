''' a = input()
print('a is '+a)
if a==1 :
    print('apple')
else:
    if a==2:
        print('orange')
    else:
        if a==3:
            print('banana')
        else:
            print('shopping') '''

#将上述代码进行优化，elif不能单独出现
a = input()
print('a is '+a)
if a=='1' :
    print('apple')
elif a=='2':
    print('orange')
elif a=='3':
     print('banana')
else:
    print('shopping')

#上述代码有问题，不管你输入a为什么，都会走到最终的shopping
#a在做比较运算的时候出现了问题，a在终端中输入的1，在终端input是字符串，不是数字
#解决方法1：如上一段代码所示。把比较的后面改成字符串
#解决方法2: a=int(a) 把a改成整型 

# 课后小练习
# a=1 b=0 a,b不能同时为false，返回为真的变量
# 除了if/else，也可以使用or这个运算符




