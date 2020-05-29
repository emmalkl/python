'''
一段关于条件控制的小程序
'''

''' mood=True
if mood:
    print('go to left')
    #print('back away')#没有缩进的时候就当作一句话处理 
else:
    print('go to right') '''


# 真实情况下使用条件控制语句
account = 'lilin'
password = '123456'
print('请输入account')
user_account = input() #此函数为用户输入的操作
print('请输入password')
user_password = input()
# 如果用户名密码相同，打印success，不同的话打印fail
if user_account==account and user_password==password :
    print('success')
else:
    print('fail')


