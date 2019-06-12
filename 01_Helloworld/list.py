# 列表 List
names = ['xiaoming', 'xiaohong']
print(names)

# 访问列表元素
citys = ['南京', '杭州', '厦门', '青岛']
print(citys[0])
print(citys[1])
print(citys[-1])
print(citys[-2])
print("我最喜欢的城市：" + citys[-1])

# 数字列表
nums = [11, 2, 36, 90]
# print("我最喜欢的数字：" + nums[1]) 报错
print("我最喜欢的数字：" + str(nums[1]))

# 任意类型元素组成的列表
members = [11, "淮安", '青岛', 90]
print("第2个元素：" + members[1])

# 修改元素值
members = [11, "淮安", '青岛', 90]
members[0] = 'xiao'
print(members)

# 添加元素
## 末尾添加
members = [11, "淮安", '青岛', 90]
members.append('红')
print(members)
## 空列表末尾添加
members = []
members.append('红')
members.append(12)
print(members)
## 指定位置添加
members = [11, "淮安", '青岛', 90]
members.insert(1, 50)
print(members)

# 删除元素
## 直接删除
members = [11, "淮安", '青岛', 90]
print(members)
del members[0]
print(members)

## pop删除
members = [11, "淮安", '青岛', 90]
print("删除前列表:" + str(members))
item = members.pop()
print("被删除元素：" + str(item))
print("删除后列表:" + str(members))

## pop指定索引删除
members = [11, "淮安", '青岛', 90]
print("删除前列表:" + str(members))
item = members.pop(2)
print("被删除元素：" + str(item))
print("删除后列表:" + str(members))

## 根据值删除
members = [11, "淮安", '青岛', 90, 90]
print("删除前列表:" + str(members))
members.remove(90)
print("删除后列表:" + str(members))

# 排序列表
## 按照首字母正排序
members = ['windows', 'Apple', 'oracle', 'ibm']
members.sort()
print(members)
## 按照首字母反排序
members = ['windows', 'Apple', 'oracle', 'ibm']
members.sort(reverse=True)
print(members)

## 临时排序：不改变列表本身
members = ['windows', 'Apple', 'oracle', 'ibm']
members2 = sorted(members)
members3 = sorted(members, reverse=True)
print("\n排序后内容：" + str(members2))
print("倒排序后内容：" + str(members3))
print("原有列表：" + str(members))

## 数字排序
members = [23, 1, 78, 13]
members2 = sorted(members)
print("\n排序后内容：" + str(members2))
print("原有列表：" + str(members))

# 反转列表
members = [11, "淮安", '青岛', 90]
members.reverse()
print(members)
members.reverse()
print(members)

# 确定列表长度
members = [11, "淮安", '青岛', 90]
print("列表长度：" + str(len(members)))