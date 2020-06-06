''' a=1
b=2
c=3 '''

#以上三行代码可以简化
a,b,c=1,2,3

d=1,2,3
print(type(d))#tuple
a,b,c=d #序列解包


a,b=[1,2,3]#报错


#下面这种情况
a=1
b=1
c=1

#a,b,c=1,1,1
a=b=c=1
print(a,b,c)