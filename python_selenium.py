from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium

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

# #查找元素
# browser.get('http://www.taobao.com')
# print(browser.page_source)
# #通过三种不同的方式去获取响应的元素，第一种是通过id的方式，第三个中是CSS选择器，第二种是xpath选择器，结果都是相同的
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_xpath('//*[@id ="q"]')
# input_third = browser.find_element_by_css_selector("#q")
# input_fourth = browser.find_element(By.ID,'q')
# #多元素查找
# lis = browser.find_elements_by_css_selector('.service-bd li')
# lis1 = browser.find_elements_by_css_selector('.layer .layer-inner')
# lis2 = browser.find_elements(By.ID,'J_TBBucket')
# print(input_first)
# print(input_second)
# print(input_third)
# print(input_fourth)
# print(lis)
# print(lis1)
# print(lis2)
# browser.close()
#
#
# #元素交互操作
# browser.get('http://www.taobao.com')
# input_str = browser.find_element_by_id('q')
# input_str.send_keys('ipad')
# time.sleep(1)
# input_str.clear()
# input_str.send_keys('Mac Pro')
# button =  browser.find_element_by_class_name('search-button')
# time.sleep(1)
# button.click()

#交互动作
from selenium.webdriver import ActionChains
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')
time.sleep(5)
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()







