import urllib.request
import os
import time

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('UserAgent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    print(url)
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_address = []

    a = html.find('img src=')

    while a!= -1:
        b = html.find('jpg',a,a+255)

        if b!= -1:
            img_address.append('http:'+html[a+9:b+3])
        else:
            b = a + 9
        a = html.find('img src=',b)

    for each in img_address:
#       print(each)
        return img_address


def save_img(folder,img_address):
    for each in img_address:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder='img',pages=10000):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num = i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_address = find_imgs(page_url)
        save_img(folder,img_address)
        time.sleep(10)

if __name__ == '__main__':
    download_mm()