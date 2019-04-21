from bs4 import BeautifulSoup

# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''
#
# # soup = BeautifulSoup(html,'lxml')
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.title.parent.name)
# # print(soup.p)
# # print(soup.p["class"])
# # print(soup.a)
# # print(soup.find_all('a'))
# # print(soup.find(id='link2'))
# # print(soup.find(href="http://example.com/tillie"))
#
# # for link in soup.find_all('a'):
# #     print(link.get('href'))
# # print(soup.get_text)
#
#
# #基本使用
# # print(soup.title)
# # print(type(soup.title))
# # print(soup.head)
# # print(soup.p)
# #获取标签名称
# # print(soup.title.name)
# # print(soup.p.name)
#
# #获取属性
# # print(soup.p['name'])
# # print(soup.p.attrs['name'])
#
# #获取内容
# # print(soup.p.string)
#
# #子节点和子孙节点
#
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html,'lxml')
# # print(soup.p.contents)
#
# #children的使用
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i,child)

#标准选择器
#find_all find_all(name,attrs,recursive,text,**kwargs)
#name属性
html1='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup1 = BeautifulSoup(html1,'lxml')
# print(soup1.find_all('ul'))
# print(soup1.find_all('ul')[0])

# for ul in soup1.find_all('ul'):
#     print(ul.find_all('li'))

#attrs
# print(soup1.find_all(attrs={"id" : "list-1"}))
# print(soup1.find_all(attrs={"name" : "elements"}))

#text
print(soup1.find_all(text = 'Foo'))

#find find(name,attrs,recursive,text,**kwargs) find返回的匹配结果的第一个元素


#CSS选择器
print(soup1.select('.panel .panel-heading'))
print(soup1.select('ul li'))
print(soup1.select('#list-2 .element'))

#获取内容 通过get_text()就可以获取文本内容
for li in soup1.select('li'):
    print(li.get_text())

#获取属性 或者属性的时候可以通过[属性名]或者attrs[属性名]
for ul in soup1.select('ul'):
    print(ul['id'])
    print(ul.attrs['class'])

