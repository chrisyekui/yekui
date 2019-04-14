import requests
url = "http://www.baidu.com"
strhtml = requests.get(url)

print(type(strhtml))
print(strhtml.status_code)
print(type(strhtml.text))
print(strhtml.text)
print(strhtml.cookies)
print(strhtml.content)
print(strhtml.content.decode("utf-8"))

requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")

response = requests.get("http://httpbin.org/get")
print(response.content.decode("utf-8"))

response1 = requests.get("http://httpbin.org/get?name=zhaofan&age=23")
print(response1.text)

data = {"name":"zhangsan","age":"23"}
response2 = requests.get("http://httpbin.org/get",params=data)
print(response2.url)
print(response2.text)

#####解析json#######
import json

response3 = requests.get("http://httpbin.org/get")
print(type(response3.text))
print(response3.json())
print(json.loads(response3.text))
print(type(response3.json()))

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
response4 = requests.get("http://www.zhihu.com",headers = headers)
print(response4.text)

data1 = {"name":"zhangsan","age":"24"}
response5 = requests.post("http://httpbin.org/post",data = data1)
print(response5.text)

response6 = requests.get("http://www.baidu.com")
print(type(response6.status_code),response6.status_code)
print(type(response6.headers),response6.headers)
print(type(response6.cookies),response6.cookies)
print(type(response6.url),response6.url)
print(type(response6.history),response6.history)

response7 = requests.get("http://www.baidu.com")
if response7.status_code == requests.codes.ok:
    print(requests.codes.ok)
    print("访问成功")

#######文件上传########
files = {"files":open("莫失莫忘.eop","rb")}
response8 = requests.post("http://httpbin.org/post",files = files)
print(response8.text)

#######获取cookies########
response9 = requests.get("http://www.baidu.com")
print(response9.cookies)
for key,value in response9.cookies.items():
    print(key + "=" + value)

#######会话维持########
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/666666")
response10 = s.get("http://httpbin.org/cookies")
# print(response10.text)

#######证书验证########
response11 = requests.get("https://www.12306.cn")
print(response11.status_code)