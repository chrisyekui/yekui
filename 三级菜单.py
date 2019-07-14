menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

location = menu
location_list = []
while True:
    #打印当前层级list
    print(str(list(location.keys())))
    choose = input('【back返回,quit退出】请输入您的选择:').strip()
    if choose in location:
        location_list.append(location)
        location = location[choose]
    elif choose == 'back':
        if location_list:
            location = location_list.pop()
    elif choose == 'quit':
        break
    else:
        print('输入有误，请重新输入')
