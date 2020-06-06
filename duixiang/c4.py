class Student():
    # name='默认name'#类变量
    # age=0
    sum=0#一个班级所有学生的总数
 
    def __init__(self,name,age):
        self.name=name#实例变量
        self.age=age#实例变量

    def do_homework(self):
        print('do_homework')

student1=Student('liiln1',20)
print(student1.name)
# student2=Student(age=201)
# print(student2.name)#缺少必须参数
# student3=Student('liiln3')
# print(student3.name)
# print(Student.name)