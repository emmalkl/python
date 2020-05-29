# 循环
# while/for
#while else是在循环被打印出来之后打印出来

''' CONDITION = True
while CONDITION:
    print('会一直循环死循环，crtl+c结束') '''

counter=1
while counter<=10:
    counter+=1
    print(counter)
else:
    print('EOF')
    
# 递归用while，其它循环用for
