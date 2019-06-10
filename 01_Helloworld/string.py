# 直接用引号表示的内容就是字符串
address = '中国江苏'
print(address)
# 单引号、双引号都可以表示字符串
address = "中国南京"
print(address)

# 如果要在字符串中表示字符串，需要注意和语法定义的字符表示相反
address = '江苏是"东部沿海省份"'
print(address)
address = "江苏是'东部沿海省份'"
print(address)

# 首字母大写
message = 'nanjing is a city'
print(message.title())

# 字符全部大写
print(message.upper())
# 字符全部小写
print(message.lower())

# 字符串拼接
message1 = 'nanjing is a city'
message2 = 'huaian is also a city'
print(message1 + " , " + message2)

# 制表符
message = '\tnanjing is a city'
print(message)
# 换行
message = 'nanjing \n\tis a city'
print(message)

# 去掉左侧空格
message = '  nanjing is a city'
print(message.lstrip())
# 去掉右侧空格
message = '  nanjing is a city  '
print(message.rstrip())
# 去掉左右两侧空格
message = '  nanjing is a city  '
print(message.strip())
print(message)