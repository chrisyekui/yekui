import requests
import os
from bs4 import BeautifulSoup
import time
import re

main_page_content = requests.get('https://www.autohome.com.cn/huhehaote/').text

main_page = BeautifulSoup(main_page_content,'html.parser')
# print(main_page)

main_div = main_page.find(name='div',attrs={'class':'people-content'})
main_ul = main_div.find(name='ul',attrs ={'class':'list-text'})

main_a_list = main_ul.find_all(name='a')
print(main_a_list)
n = 1
for a in main_a_list:
    one_page_url = 'https:'+a.get('href')
    # print(one_page_url)
    one_page_content = requests.get(one_page_url).text
    one_page_content = one_page_content.replace('</br>','')
    one_page = BeautifulSoup(one_page_content,'html.parser')
    img_list = one_page.find('div',attrs={'class':'journey-item-list'}).find_all('img')
    print(img_list)
    for img in img_list:
        download_url = img.get('data-original')
        if not download_url:
            download_url = img.get('src')
        print(download_url)
        f = open('img1/汽车之家图片%s.jpg' %n,mode='wb')
        f.write(requests.get(download_url).content)
        f.close()
        n = n+1
        print('您成功从汽车之家偷取一张图片')




