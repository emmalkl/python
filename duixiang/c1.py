

#定义类，类的名字首字母大写如：StudentHomework
#函数的（）参数与类不同
class Student():
    name=''#全局变量
    age=0
    #类中编写函数的时候与普通函数有个区别self
    #self.name
    #行为，方法
    def print_file(self):
        print('name:'+self.name)
        print('age:'+str(self.age))

#调用类:把类进行实例化
# student = Student()
#调用类的方法
# student.print_file()

#类的基本作用就是在封装代码

class StudentHomework():
    homework_name=''

#类与对象关系是什么。。
