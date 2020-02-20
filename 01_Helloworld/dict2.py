# -------------字典2-------------
# 字典嵌套使用

# 字典列表：多个字典组成列表
student_0 = {'name': '小明', 'age': 10, 'address': '淮安市'}
student_1 = {'name': '小红', 'age': 12, 'address': '南京市'}
student_2 = {'name': '小丽', 'age': 15, 'address': '青岛市'}

students = [student_0, student_1, student_2]
for student in students:
    print(student)

# 在字典中存储列表
person = {'name': '小明', 'books': ['语文','数学','物理']}
print(person['books'])

for book in person['books']:
    print(book)

# 在字典中存储字典
person = {
    'name': '小明', 
    'books': {
        'first':'语文',
        'second':'数学',
        'third':'英文'
    }
}

print(person['books'])

for key,value in person.items():
    if 'books' == key:
        for k,v in value.items():
            print(k + ' ' + v)

