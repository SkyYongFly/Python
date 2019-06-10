# 字符串实例文件

# 可以使用单引号，也可以使用双引号表示字符串
address = '中国江苏'
print(address)
address = "中国南京"
print(address)

# 如果需要在字符串中显示引号，需要注意语句中引号表示与语法相反
address = '江苏是"东部沿海省份"'
print(address)
address = "江苏是'东部沿海省份'"
print(address)

# 首字母大写方法
address = 'nanjing is a city'
print(address.title())
# 字符全部大写
print(address.upper())
# 字符全部小写
address = 'nanJING Is a city'
print(address.lower())

# 合并字符串
address2 = 'huaian is also a city'
print(address + " , " + address2)

# 制表符
address = '\tnanjing is a city'
print(address)
# 换行符
address = 'nanjing \n\tis a city'
print(address)

# 删除左空白
address = ' nanjing is a city'
print(address.lstrip())
# 删除右空白
address = ' nanjing is a city  '
print(address.rstrip())
# 删除左右空白
address = '  nanjing is a city  '
print(address.strip())
print(address)