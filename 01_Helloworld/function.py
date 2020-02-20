# --------------函数-----------------

# 定义函数
def get_user_name():
    print('我的名字是：小明')
# 调用函数
get_user_name()

# 函数传参
def get_user_name(name):
    print('我的名字是：' + name)
# 调用
get_user_name('小华')

# 多个参数
def get_user_info(name, age):
    print('我的名字是：' + name + '，年龄：' + str(age))
# 调用
get_user_info('小美', 12)
# 指定参数名称调用
get_user_info(age = 15, name = '小琴')

# 定义形参默认值
def get_user_info(name, city = '南京市'):
    print('我的名字是：' + name + '，来自：' + city)
# 调用：使用默认值参数
get_user_info('小艾')
# 调用：指定参数值
get_user_info('小艾', '扬州市')

# 函数返回值
def get_user_info(name):
    return '我的名字是：' + name
# 调用
msg = get_user_info('小强')
print(msg)

# 返回列表
def get_persons():
    return ['小明','小丽','小花','小艾']
# 调用
print(get_persons())

# 传递列表，并修改（直接作用于原列表）
def need_books(books):
    while '英语' in books:
        books.remove('英语')
    return books
# 调用
books = ['语文','数学','英语']
print(books)
print(need_books(books))
print(books)

# 传递列表，不允许修改（传递副本，不影响原列表）
def need_books(books):
    while '英语' in books:
        books.remove('英语')
    return books
# 调用
books = ['语文','数学','英语']
print(books)
print(need_books(books[:]))
print(books)

# 任意数量参数（*形参名称  用一个空元组接收）
def get_books(*books):
    print(books)
# 调用
get_books('语文')
get_books('语文','数学')

# 任意数量字典参数(**形参名称  用一个空字典接收)
def get_books(**books):
    for key,val in books.items():
        print(key + ' : ' + val)
# 调用
get_books(first='语文', second='数学')