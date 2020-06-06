
""" for(i=0;i<10;i++){

} """

# for each
# a=[1,2,3,4,5,....]

#range函数，从0开始有10个数字。
""" for x in range(0,10):
    print(x) """
#结果:打印0~9

""" for x in range(0,10,2):
    print(x,end='|') """
#结果：0|2|4|6|8|

""" for x in range(10,0,-2):
    print(x,end='|') """
#结果:10|8|6|4|2|

a=[1,2,3,4,5,6,7,8]#打印间隔数1，3，5，7
""" for i in range(0,len(a),2):
    print(a[i],end='|') """
#结果:1|3|5|7|
#或者方法2:切片
b=a[0:len(a):2]
print(b)
#结果:[1, 3, 5, 7]

