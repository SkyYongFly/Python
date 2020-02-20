# 条件判断

citys = ('南京','旧金山','青岛','淮安', '洛圣都')

# if else
for city in citys:
    if city == '淮安':
        print('我的家乡：' + city)
    else:
        print('其它城市: ' + city)

# and or 
# 判断是否在列表 in
if '青岛' in citys or '无锡' in citys:
    print("青岛或无锡在列表中")

# if elif else
age = 890
if age < 10:
    print("少年")
elif age < 20: 
    print("骚年")
elif age < 60: 
    print("青年")
else:
    print("老年")

# 判断集合是否为空
citys = []
if citys:
    print("列表不为空")
else:
    print("列表为空")

