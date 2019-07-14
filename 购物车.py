
shopping_list = {}
account_money_list = {}

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]

def login():
    # account = 'User'
    # password = '123456'
    account = input('请输入账号:')
    password = input('请输入密码')
    if account == 'User' and password == '123456':
        print('登录成功,请继续')
    else:
        exit('账号密码输入错误，请重试')

login()

# def productlist():
