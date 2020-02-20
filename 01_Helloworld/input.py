# -------------输入函数-------------

name = input('请输入你的名字：')
print('你的名字是：' + name)

age = input('请输入你的年龄：')
age = int(age)
if age >= 18:
    print('成年人啦')