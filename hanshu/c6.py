def print_student_files(name,gender='nan',age=20,
                        college='qinghua'):
    print('我叫'+str(name))
    print('我今年'+str(age)+'岁')
    print('我是'+str(gender)+'生')
    print('我在'+str(college)+'上学')

print_student_files('lilin','nv',19,'jialidun')
print('~~~~~~~~~~~~~~~~~~~~~')
print_student_files('lilin')
print('~~~~~~~~~~~~~~~~~~~~~')
print_student_files('lilin',age=30)
print('~~~~~~~~~~~~~~~~~~~~~')
# print_student_files('lilin',gender='nv',30,college='beida')#报错

#注意：不能把非默认参数放在默认参数之后
