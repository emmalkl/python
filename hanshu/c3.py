# R skill1,skill2 返回多个参数
def damage(skill1,skill2):
    damage1=skill1*3
    damage2=skill2*10+2
    return damage1,damage2
damage=damage(3,6)
print(damage)#(9, 62)是个元组
print(type(damage))#<class 'tuple'>
print(damage[0],damage[1])#这个写法是不好的，如果想提取元组中的某个元素
#skill1_damage,skill2_damage=damage(3,6)
#print(skill1_damage,skill2_damage)
#这种方式叫做：序列解包
