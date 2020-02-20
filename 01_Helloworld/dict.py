# ------------字典-----------
# 类似Map数据结构

person = {'name': '小明', 'age': 10}
print("姓名：" + person['name'])
print("年龄：" + str(person['age']))

# 动态添加键值对
person['address'] = '江苏省淮安市'
print(person)   

# 修改属性值
person['age'] = 12
print(person)

# 删除键值
del person['age']
print(person)

# 遍历字典
person = {'name': '小明', 'age': 10, 'address': '江苏省淮安市'}
for key, value in person.items():
    print(key + " : " + str(value))
# 遍历变量可以使用任何名称
for k, val in person.items():
    print(k + " : " + str(val))

# 遍历健
for key in person.keys():
    print(key)

# 遍历值
for val in person.values():
    print(val)

person = {'name': '小明', 'address': '江苏省淮安市', 'age': 10}
# 遍历是无序的，可以排序
for key in sorted(person.keys()):
    print(key)

# 可以使用set()去重
for val in set(person.values()):
    print(val)
