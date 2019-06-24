import requests
import os
import time
import re
from selenium import webdriver


def url_open(url):
    headers = {
        'UserAgent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    return html

#主程序
def get_class(url):
    html = url_open(url)
    get_class = []
    results = re.findall('<li.*?href=\'\/(.*?)\/\'\s><span>(.*?)</span></a></li>',html,re.S)
    print(results)
    for result in results:
        print(result[1])
        #已有目录不用重新创建
        if os.path.exists(result[1]):
            os.chdir(result[1])
        else:
            os.mkdir(result[1])
            os.chdir(result[1])
        class_url = 'https://www.mn52.com/'+result[0]
        print(class_url)
        #打开分类链接
        # url_open(class_url)
        get_max_pagenum(class_url)
        get_classpage_message(class_url)






        os.chdir(os.path.pardir)



def get_max_pagenum(url):
    try:
        html = url_open(url)
        max_pagenum = re.findall('下一页</a>\r\n<a href=\'list_.*?_(.*?).html\'>末页</a>.*?<!-- page end -->',html,re.S)
        print(max_pagenum[0])
        return max_pagenum[0]
    except:
        #获取不到最大页面时返回30
        return 30

def get_classpage_message(url):
    html = url_open(url)
    classpage_messages = re.findall('<div class="picbox">.*?<a href="(.*?)" target="_blank"><img src=.*?data-original=.*?alt="(.*?)" width="235" height="350" style="display: inline;"></a>', html, re.S)
    print(classpage_messages)
    for classpage_message in classpage_messages:
        print(classpage_message)
        concretePicture_url = "https://www.mn52.com"+classpage_message[0]
        if os.path.exists(str(classpage_message[1])):
            os.chdir(classpage_message[1])
        else:
            os.mkdir(classpage_message[1])
            os.chdir(classpage_message[1])
        os.chdir(os.path.pardir)
        # time.sleep(2)
        get_PicturepPage_nums(concretePicture_url)
        get_Picture_downloadurl(concretePicture_url)

    return concretePicture_url

def get_PicturepPage_nums(url):
    html = url_open(url)
    PicturePage_nums = re.findall('<div class="img-wrap"><a href="javascript:;" hidefocus="true"><img src=.*?title="第(.*?)张" rel=.*?>', html, re.S)
    # print(PicturePage_nums)
    print(PicturePage_nums[-1])
    #返回页码的最大值
    return PicturePage_nums[-1]

def get_Picture_downloadurl(url):
    html = url_open(url)
    Picture_vague_urls = re.findall('<div id="content".*?<div id="big-pic">\r\n(.*?)<div class="photo_prev">', html, re.S)
    picture_real_urls = re.findall('<img src="(.*?)" />',str(Picture_vague_urls),re.S)
    print(picture_real_urls)
    for picture_real_url in picture_real_urls:

















# def get_page(url):
#     html = url_open(url).decode('utf-8')
#     print(html)
#
#     # a = html.find('current-comment-page') + 23
#     # b = html.find(']',a)
#     # return html[a:b]
#
# def find_imgs(url):
#     html = url_open(url).decode('utf-8')
#     print(html)
#     img_address = []
#
#
#     # a = html.find('img src=')
#     #
#     # while a!= -1:
#     #     b = html.find('jpg',a,a+255)
#     #
#     #     if b!= -1:
#     #         img_address.append('http:'+html[a+9:b+3])
#     #     else:
#     #         b = a + 9
#     #     a = html.find('img src=',b)
#
#     for each in img_address:
# #       print(each)
#         return img_address
#
#
# def save_img(folder,img_address):
#     for each in img_address:
#         filename = each.split('/')[-1]
#         with open(filename,'wb') as f:
#             img = url_open(each)
#             f.write(img)

def download_mn52_mm(folder='img',pages=10000):
    if os.path.exists(folder):
        os.chdir(folder)
    else:
        os.mkdir(folder)
        os.chdir(folder)

    url = "https://www.mn52.com/"
    # url = "https://www.mn52.com/meinvmingxing/26296.html"

    get_class(url)
    # get_PicturepPage_nums(url)


# def new_folder(floder=result)


        # page_num = int(get_page(url))
        #
        # for i in range(pages):
        #     page_num = i
        #     page_url = url + 'page-' + str(page_num) + '#comments'
        #     img_address = find_imgs(page_url)
        #     save_img(folder,img_address)
        #     time.sleep(10)

if __name__ == '__main__':
    download_mn52_mm()