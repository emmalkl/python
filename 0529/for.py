


#主要用来遍历/循环 序列或者集合、字典
''' a=['apple','orange','banana','grape']
for item in a:
    print(item) '''
#可以循环遍历list a

#b=[['apple','orange','banana','grape'],(1,2,3)]
''' for item in b:
    for y in item:
        print(y) '''
#结果是b的元素二维数组遍历之后呈列分布，要使横向补充出来
''' for item in b:
    for y in item:
        print(y,end='') '''#appleorangebananagrape123

# for与else也可以搭配,当列表中所有元素被打印出来之后else 的内容被打印出来
''' for target_list in expression_list:
    pass
else:
    pass '''



''' a=[1,2,3]
for x in a:
    if x==2:
        break
    print(x) '''

''' a=[1,2,3]
for x in a:
    if x==2:
        continue #x==2不会执行了，但是不会跳出for循环
    print(x) '''

''' a=[1,2,3]
for x in a:
    if x==2:
        break
    print(x)
else:
    print('EOF')  '''# break跳出循环也不会执行出else的print；continue会打印else的内容


#在这个情况下的break却会打印出else的内容，1，2，3也会打印出来
''' b=[['apple','orange','banana','grape'],(1,2,3)]
for item in b:
    for y in item:
        if y == 'orange':
            break
        print(y)
else:
    print('EOF') '''
#结果是：'apple' 1,2,3 'EOF'

b=[['apple','orange','banana','grape'],(1,2,3)]
for item in b:
    if 'orange' in item:
        break
    for y in item:
        if y == 'orange':
            break
        print(y)
else:
    print('EOF')
#结果是：什么都没有输出，因为'orange' in item判断为真所以什么也没有输出，跳出循环。



