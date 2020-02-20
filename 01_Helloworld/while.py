# ---------循环 while-----------

num = 1
while num < 10:
    print(num)
    num += 1

# 使用break
print('你猜我想的是哪个数字？')
num = input('请输入：')
while True:
    if num == '0':
        print('退出程序！')
        break
    elif num == '99':
        print('恭喜你猜对啦！')
        break
    else:
        num = input('你猜错啦，重新猜一个：')

# continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue

    print('奇数: ' + str(num))

# 遍历列表
print('\n')
citys = ['南京','旧金山','青岛','淮安', '洛圣都']
while citys:
    print(citys.pop())
print(citys)

# 循环遍历列表删除
print('\n')
citys = ['南京','青岛','旧金山','青岛','淮安', '洛圣都','青岛']
while '青岛' in citys:
    citys.remove('青岛')
print(citys)
