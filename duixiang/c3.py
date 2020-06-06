''' 类是现实世界或思维世界中的实体在计算机中的反映
它将数据以及这些数据上的操作封装在一起 '''
class Student():
    name=''
    age=0
 #类变量
 #实例变量   
    def __init__(self,name,age):
        #构造函数
        # print('student')#连续打印两个student

        #初始化对象的属性
        name=name
        age=age

    def do_homework(self):
        print('do_homework')

student=Student('liiln',20)
print(student.name)


# a=student.__init__()#连续打印两个student
# print(a)#None,因为这个函数没有return任何值，而且构造函数没有办法return！！！
# print(type(a))#<class 'NoneType'>

#作用，让模板生成不同的对象


''' student1=Student()
student2=Student()
student3=Student() '''

''' 
它们在计算机中的存储位置不同
print(id(student1))
print(id(student2))
print(id(student3)) '''

