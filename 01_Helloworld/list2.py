# 循环遍历
citys = ['南京','旧金山','青岛','淮安']
for city in citys :
    print('美丽的城市：' + city)
#单独的一行
print('一起去玩，哈哈')

# 循环输出随机数
for num in range(0, 6):
    print('\t' + str(num))

# range()转为列表
print(list(range(1,6)))
# 指定range()步长为2
print(list(range(1,10, 2)))

# 最大、最小、总和
digits = list(range(1, 11))
print("数字列表： " + str(digits))
print("最大数字： " + str(max(digits)))
print("最小数字： " + str(min(digits)))
print("数字总和： " + str(sum(digits)))

# 列表解析：合并操作循环
## 循环1到10整数列表，将平方值放置到列表中
squares = [val ** 2  for val in range(1,11)]
print(squares)

# 切片
citys = ['南京','旧金山','青岛','淮安', '洛圣都']
## 取前两个元素
print(citys[0:2])
## 缺省起始位置则从头开始
print(citys[:3])
## 缺省结束位置则遍历到末尾
print(citys[2:])
## 倒序索引:获取倒数后两个元素
print(citys[-2:])

# 复制
## 如果列表直接赋值，其实是赋值引用
citys = ['南京','旧金山','青岛','淮安', '洛圣都']
citys2 = citys
citys.append('石家庄')
print(citys)
print(citys2)
## 如果值复制，创建新的列表，需要切片方式
citys3 = citys[:]
citys.append('扬州')
print(citys)
print(citys3)