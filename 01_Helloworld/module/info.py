# 导入模块
import person
# 导入指定目录模块
import module2.person as p

# 调用模块中的函数： 模块名.函数名(参数)
person.get_person_info('小丽', '淮安市')
person.get_person_age(10)

p.get_person_info('小强','青岛市')
p.get_person_age(20)