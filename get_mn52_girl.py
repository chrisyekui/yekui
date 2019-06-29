import requests
import os
import time
import re
import random


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
        if result[1] not in ['性感美女','头像集', '婚纱图片''萌宠图片']:
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
            print('不需要这几个分类图片')


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
        #过滤特殊字符，只保留中英文和数字，否则无法创建文件夹
        # str = re.sub('[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", classpage_message[1])
        str = re.sub('[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', '', classpage_message[1])
        if os.path.exists(str):
            try:
                # 此方法适合碰到一个异常解决一个异常
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
    # 打印当前时间
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    for Picture_real_url in Picture_real_urls:
        #做个间隔，发现下得太慢了，放弃
        # time.sleep(0.5)
        #网页可能不是一个人写的有时匹配到的是//image.mn52.com/img/,有时直接匹配到后面的/img
        if Picture_real_url[:3] == '//i':
            picture = 'https:' + Picture_real_url
        elif Picture_real_url[:3] == '/im':
            picture = 'https://image.mn52.com' + Picture_real_url
        else:
            picture = Picture_real_url
        filename = (picture).split('/')[-1]
        print(filename)
        #尝试使用打开浏览器方式获取，太慢，放弃，UI自动化操作还是不靠谱
        # browser = webdriver.Chrome(
        #     executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        # browser.get(picture)
        # time.sleep(2)
        # browser.close()
        with open(filename, 'wb') as f:
            # img = url_open(picture)
            #尤其注意Referer
            UserAgentlist = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
                             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                             'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                             'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                             'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
                             'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                             'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
                             'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
                             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
                             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
                             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
                             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
                             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
                             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
                             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
                             'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)']

            USER_AGENT = random.choice(UserAgentlist)
            headers1 = {
                'Referer': url,
                'User-Agent': USER_AGENT,
                'Accept': '*/*',
                'Cache-Control': 'no-cache',
                'Host': 'image.mn52.com',
                'accept-encoding': 'gzip, deflate',
                'Connection': 'keep-alive'
            }
            try:
                #设置10秒超时限制
                pic = requests.get(picture, headers=headers1, timeout = 10)
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
