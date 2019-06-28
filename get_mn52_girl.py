import requests
import os
import time
import re


def url_open(url):
    headers = {
        'Referrer': 'https://www.mn52.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'accept-encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    # print(html)
    return html


# 主程序
def get_class(url):
    html = url_open(url)
    get_class = []
    results = re.findall('<li.*?href=\'\/(.*?)\/\'\s><span>(.*?)</span></a></li>', html, re.S)
    print(results)
    for result in results:
        if result[1] not in ['头像集', '婚纱图片''萌宠图片']:
            print(result[1])
            # 已有目录不用重新创建
            if os.path.exists(result[1]):
                os.chdir(result[1])
            else:
                os.mkdir(result[1])
                os.chdir(result[1])
            class_url = 'https://www.mn52.com/' + result[0]
            print(class_url)
            # 查找分类页数并每页查找
            # for i in range(1,int(get_max_pagenum(class_url))+1):
            html1 = url_open(class_url)
            list_num = re.findall(
                '<div class="itempages">.*?<a class="current">1</a>\r\n.*?<a href=\'(.*?)_2.html\'>2</a>', html1, re.S)
            print(list_num)
            for i in range(1, int(get_max_pagenum(class_url)) + 1):
                print(class_url + '/' + list_num[0] + '_' + str(i) + '.html')
                get_classpage_message(class_url + '/' + list_num[0] + '_' + str(i) + '.html')
            os.chdir(os.path.pardir)
        else:
            print('不需要这3个分类图片')


def get_max_pagenum(url):
    try:
        html = url_open(url)
        max_pagenum = re.findall('下一页</a>\r\n<a href=\'list_.*?_(.*?).html\'>末页</a>.*?<!-- page end -->', html, re.S)
        print(max_pagenum[0])
        return max_pagenum[0]
    except:
        # 获取不到最大页面时返回30
        return 30


def get_classpage_message(url):
    html = url_open(url)
    classpage_messages = re.findall(
        '<div class="picbox">.*?<a href="(.*?)" target="_blank"><img src=.*?data-original=.*?alt="(.*?)" width="235" height="350" style="display: inline;"></a>',
        html, re.S)
    print(classpage_messages)
    for classpage_message in classpage_messages:
        print(classpage_message)
        concretePicture_url = "https://www.mn52.com" + classpage_message[0]
        #过滤特殊字符，只保留中文
        # str = re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", classpage_message[1])
        str = re.sub('[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', '', classpage_message[1])
        if os.path.exists(str):
            try:
                # os.chdir(classpage_message[1].replace(':','').replace('|',''))
                os.chdir(str)
            except NotADirectoryError:
                pass
        else:
            try:
                # os.mkdir(classpage_message[1].replace(':','').replace('|',''))
                # os.chdir(classpage_message[1].replace(':','').replace('|',''))
                os.mkdir(str)
                os.chdir(str)
            except NotADirectoryError:
                pass
        Save_Picture(concretePicture_url)
        os.chdir(os.path.pardir)
        # time.sleep(2)
        get_PicturepPage_nums(concretePicture_url)
        # Save_Picture(concretePicture_url)
    return concretePicture_url


def get_PicturepPage_nums(url):
    html = url_open(url)
    PicturePage_nums = re.findall(
        '<div class="img-wrap"><a href="javascript:;" hidefocus="true"><img src=.*?title="第(.*?)张" rel=.*?>', html,
        re.S)
    # print(PicturePage_nums)
    try:
        print(PicturePage_nums[-1])
        # 返回页码的最大值
        return PicturePage_nums[-1]
    except IndexError:
        pass



def Save_Picture(url):
    html = url_open(url)
    Picture_vague_urls = re.findall('<div id="content".*?<div id="big-pic">\r\n(.*?)<div class="photo_prev">', html,
                                    re.S)
    Picture_real_urls = re.findall('<img src="(.*?)" />', str(Picture_vague_urls), re.S)
    print(Picture_real_urls)
    for Picture_real_url in Picture_real_urls:
        # time.sleep(0.5)
        picture = 'https:' + Picture_real_url
        filename = (picture).split('/')[-1]
        print(filename)
        # browser = webdriver.Chrome(
        #     executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        # browser.get(picture)
        # time.sleep(10)
        # browser.close()
        with open(filename, 'wb') as f:
            # img = url_open(picture)
            headers1 = {
                'Referer': url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
                'Accept': '*/*',
                'Cache-Control': 'no-cache',
                'Host': 'image.mn52.com',
                'accept-encoding': 'gzip, deflate',
                'Connection': 'keep-alive'
            }
            try:
                pic = requests.get(picture, headers=headers1)
                # print(pic.text)
                f.write(pic.content)
            except Exception as e:
                pass
            continue


def download_mn52_mm(folder='img', pages=10000):
    if os.path.exists(folder):
        os.chdir(folder)
    else:
        os.mkdir(folder)
        os.chdir(folder)
    url = "https://www.mn52.com/"
    get_class(url)


if __name__ == '__main__':
    download_mn52_mm()
