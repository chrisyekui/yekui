from selenium import webdriver
import time
#
# help(webdriver)
# browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path =r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
# browser = webdriver.Firefox()

# browser.get('http://www.baidu.com')
# print(browser.page_source)
# time.sleep(5)
# browser.close()

#查找元素
browser.get('http://www.taobao.com')
# print(browser.page_source)
#通过三种不同的方式去获取响应的元素，第一种是通过id的方式，第三个中是CSS选择器，第二种是xpath选择器，结果都是相同的
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_xpath('//*[@id ="q"]')
input_third = browser.find_element_by_css_selector("#q")
print(input_first)
print(input_second)
print(input_third)
browser.close()

