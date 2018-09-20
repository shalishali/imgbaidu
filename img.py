#-*- coding:utf-8 -*-
#2018年9月21日01:09:05
#具体功能就是 实现了输入关键字在百度图片中爬取前一页的图
import re
import requests

url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1537462019354_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1537462019355%5E00_1519X722&word=%E6%BC%AB%E5%A8%81'

word = input("Input key word: ")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
# result = requests.get(url)

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print(each)
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
        continue
    string = 'D:\py\pycharm\imgbaidu\poho' +  '_' + str(i) + '.jpg'
    #妈蛋 我还不知道怎么回事，自己不能创建文件件，只能相对存放 不管了先睡了

    fp = open(string,'wb') #打开 以二进制打开只能写入  文件不存在则自动创建
    fp.write(pic.content) #写入指定字符串 取图片，文件使用content
    fp.close() #关闭文件
    i += 1

