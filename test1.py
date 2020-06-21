import requests
import os
import json
import time
import shutil
import re
from bs4 import BeautifulSoup
import random
import csv
import get_proxy_pool_test



def download_apks():
    apkurls = {
        "WiFi万能钥匙":"https://wap1.hispace.hicloud.com/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum=1&maxResults=25&uri=app%7CC36902&zone=&locale=zh_CN",
        "今日头条":"https://wap1.hispace.hicloud.com/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum=1&maxResults=25&uri=app%7CC57236&zone=&locale=zh_CN"

    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    apknames = ["WiFi万能钥匙","今日头条"]
    for apkname in apknames:
        # 判断文件夹是否已存在，不用重复创建
        if os.path.exists(apkname):
            os.chdir(apkname)
        else:
            os.mkdir(apkname)
            os.chdir(apkname)
        #提取url
        url = apkurls[apkname]
        print(url)
        content = requests.get(url, headers=headers)
        print(content.text)
        data = json.loads(content.text)
        #获取downloadurl
        apk_download_url = data["layoutData"][1]["dataList"][0]["downurl"]
        try:
            # 设置60秒超时限制，下载apk包
            # apk = requests.get(apk_download_url, headers=headers, timeout=60)
            apk = requests.get(apk_download_url, headers=headers, timeout=60, proxies=proxies)
            #重命名下载下来的文件名
            filename = apkname + '0.apk'
            with open(filename,'wb') as f:
                f.write(apk.content)
            os.system('apktool d -s -f ' + filename)
            time.sleep(5)
            #进入反编译文件夹
            os.chdir(apkname + '0')
            with open('apktool.yml', 'r') as f:
                for line in f:
                    try:
                        if "versionCode" in line:
                            version = line.split("versionCode: '")[1].split("'")[0]
                            print(version)
                            print(os.getcwd())
                            # print(local_host + '\\' + apkname + '\\' + apkname + '0')
                            # print(os.listdir(os.getcwd(apkname)))
                            #返回上一级页面
                            os.chdir(os.path.pardir)
                            print(os.getcwd())
                            print(os.listdir(os.getcwd()))
                            file_list = os.listdir(os.getcwd())
                            if (version + '.apk') not in file_list:
                                #更改文件名为版本号
                                try:
                                    os.rename(filename, version + '.apk')
                        #             # os.system('rm -rf '+ apkname + '*')
                        #             # f = open('apk_version.csv', 'a+', encoding='utf-8',newline='')
                        #             # csv_writer = csv.writer(f)
                        #             # csv_writer.writerow([downloadurl, version])
                        #             # f.close()
                                    print('rename file success')
                                except Exception as e:
                                    print(e)
                                    print('rename file fail')
                    except Exception as e:
                        # os.chdir(os.path.pardir)
                        print('解析失败')
                        print(e)
                        # os.system('rm -rf testapk*')
                        # f = open('downloadurl1.csv', 'a+', encoding='utf-8', newline='')
                        # csv_writer = csv.writer(f)
                        # csv_writer.writerow([downloadurl, 'apktool.yml内未找到版本号'])
                        # f.close()
                        pass

        except Exception as e:
            pass
        # Save_apk(apk_download_url)
        # print(data["layoutData"][1]["dataList"][0]["downurl"])
        os.chdir(os.path.pardir)
        # get_class(url)




if __name__ == '__main__':
    local_host = "F:\Python_file\yekui"
    proxies = {"http": get_proxy_pool_test.get_user_ip()}
    download_apks()