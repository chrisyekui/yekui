import requests, re
from bs4 import BeautifulSoup as bs
import json
import random


def get_html(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        # html = requests.get(url=url, headers=headers)
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('error , not open page by url:' + url)


def get_proxy_ip(html):
    html = bs(html, 'html.parser')
    # print(html)
    proxy_ips = html.find(id='ip_list').find_all('tr')
    proxy_ip_list = []
    #取5-10列
    for proxy_ip in proxy_ips[6:11]:
        if len(proxy_ip.select('td')) > 0:
            ip = proxy_ip.select('td')[1].text
            port = proxy_ip.select('td')[2].text
            protocol = proxy_ip.select('td')[5].text
            time  = proxy_ip.select('td')[8].text
            # protocollists = ['http', 'https', 'HTTP', 'HTTPS']
            protocollists = ['http', 'https', 'HTTP', 'HTTPS']
            #排除存活时长‘1分钟’的ip
            if protocol in protocollists and time != '1分钟':
                # proxy_ip_list.append(f'{protocol}://{ip}:{port}')
                proxy_ip_list.append(protocol + '://' + ip + ':' + port)
    return proxy_ip_list

    # return proxy_ip_list,ip,port,protocol


def check_proxy_avaliability(ip):
    url = 'https://www.qq.com'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        proxies = {}
        if ip.startswith(('HTTPS', 'https')):
            proxies['HTTPS'] = ip
        else:
            proxies['HTTP'] = ip
        r = requests.get(url=url, headers=headers, proxies=proxies, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text, status_code = r.text, r.status_code
        # print(status_code)
        if status_code == 200:
            print('有效IP, ', ip)
            return True
        else:
            print('无效IP, ', ip)
            return False
    except:
        print('error  ', url)
        return False

def proxy_ip():
    # 代理池
    proxy_ip_list = []
    url = 'https://www.xicidaili.com/'
    protocollists = ['http', 'https', 'HTTP', 'HTTPS']
    html = get_html(url)
    ips = get_proxy_ip(html)
    print(ips)
    # use_ip_list = []
    # for ip in ips:
    #     if check_proxy_avaliability(ip):
    #         use_ip_list.append(ip)
    # return use_ip_list

def get_user_ip():
    proxy_ip_list = []
    url = 'https://www.xicidaili.com/wt'
    protocollists = ['http', 'https', 'HTTP', 'HTTPS']
    html = get_html(url)
    ips = get_proxy_ip(html)
    use_ip_list = []
    for ip in ips:
        if check_proxy_avaliability(ip):
            use_ip_list.append(ip)
    print(use_ip_list)
    #转小写
    user_ip = str.lower(random.choice(use_ip_list))
    print(user_ip)
    # userip = user_ip.split('://')
    # print(userip)
    # print("%s,%s" % (userip[0].lower(), userip[1]))
    return user_ip


if __name__ == '__main__':
    get_user_ip()
#     proxy_ip_list = []
#     url = 'https://www.xicidaili.com/'
#     protocollists = ['http', 'https', 'HTTP', 'HTTPS']
#     html = get_html(url)
#     ips = get_proxy_ip(html)
#     print(ips)
#     get_user_ip()
    # use_ip_list = []
    # for ip in ips:
    #     if check_proxy_avaliability(ip):
    #         use_ip_list.append(ip)
    # user_ip = random.choice(use_ip_list)
    # # print('有效代理ip')
    # print(user_ip)
    # print(random.choice(use_ip_list))
