import re
import requests

content= "hello 123 4567 World_This is a regex Demo"
#常规匹配
result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
result1 = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
#result.group()获取匹配的结果
print(result.group())
#result.span()获去匹配字符串的长度范围
print(result.span())

#泛匹配
result2 = re.match("^hello.*Demo$", content)
print(result2.group())

#匹配目标
# result3 = re.match('^hello\s{\d+}\s\d{4}.*Demo$',content)
content1= "hello 1234567 World_This is a regex Demo"
result3 = re.match('^hello\s(\d+)\sWorld.*Demo$', content1)
print(result3)
print(result3.group())
print(result3.group(1))

#贪婪匹配
result4 = re.match('^hello.*(\d+).*Demo$', content1)
print(result4)
print(result4.group())
print(result4.group(1))
#需要匹配到1234567
result5 = re.match('^hello.*?(\d+).*Demo$', content1)
# result5 = re.match('hello (\d+) World_This is a regex Demo', content1)
print(result5)
print(result5.group())
print(result5.group(1))

#匹配模式,很多时候匹配的内容是存在换行的问题的，这个时候的就需要用到匹配模式re.S来匹配换行的内容
content2 = """hello 123456 world_this
my name is zhaofan
"""
result6 = re.match('^hello.?(\d+).*zhaofan$', content2, re.S)
print(result6)
print(result6.group())
print(result6.group(1))

#转义
content3 = "price is $5.00"
result7 = re.match('^price is \$5\.00',content3)
print(result7.group())


#re.search
content4 = "extra things hello 123455 world_this is a Re Extra things"
result8 = re.search('hello.*?(\d+).*Re',content4)
print(result8)
print(result8.group())
print(result8.group(1))

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
result9 = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)
print(result9)
print(result9.group())
print(result9.group(1))
print(result9.group(2))

#re.findall 搜索字符串，以列表的形式返回全部能匹配的子串
result10 = re.findall('<li.*?href="(.*?)" singer="(.*?)">(.*?)</a>',html,re.S)
print(result10)
print(type(result10))
for i in result10:
    print(i)
    print(i[0],i[1],i[2])


#re.sub 替换字符串中每一个匹配的子串后返回替换后的字符串;re.sub(正则表达式，替换成的字符串，原字符串)


content5 = "Extra things hello 123455 World_this is a regex Demo extra things"
result11 = re.sub("\d+",'yekui',content5)
print(result11)
#这里需要注意的一个问题是\1是获取第一个匹配的结果，为了防止转义字符的问题，我们需要在前面加上r
result12 = re.sub('(\d+)',r'\1 789',content5)
print(result12)


#豆瓣练习
content6 = requests.get("https://book.douban.com/")
# print(content6.text)
pattern = re.compile('<li.*?cover.*?src="(.*?)".*?"more-meta".*?title=">(.*?)".*?author">(.*?)</span.*?year"></span>.*?publisher">(.*?)</span>.*?</li>',re.S)
result13 =re.findall(pattern,content6.text)
print(result13)