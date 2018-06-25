# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, itchat, re


"""
类说明: 获取糗事百科的段子 发送给女朋友或好友
Parameters:
    无
Returns:
    无
Modify:
    2018-05-28
"""
class getJoke(object):

    def __init__(self):
        self.url = 'https://www.qiushibaike.com'
        self.headers = {
            'User_agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
        }

    """ 
    类型说明: 获取网页源码
    Parameters:
        无
    Return:
        获取到的段子内容
    """
    def getText(self):
        r = requests.get(url=self.url, headers=self.headers)
        r.encoding = 'utf-8'
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        div = bf.find_all('div', class_ = 'article')[0]
        content_box = div.find('div', class_ = 'content')
        content = content_box.find('span')
        contentForAll = content_box.find('span', class_ = 'contentForAll')
        if contentForAll:
            text = self.detailText(div)
            return text
        text = re.sub('\s', '', content.getText()) # 去除空白
        return content.getText()

    """ 
    类型说明: 字数过多进去详情获取
    Parameters:
        article
    Return:
        段子详情
    """
    def detailText(self, article):
        a = article.find('a', class_ = 'contentHerf')
        href = a.get('href')
        r = requests.get(url=self.url+href, headers=self.headers)
        r.encoding = 'utf-8'
        html = r.text
        bf = BeautifulSoup(html, 'html.parser')
        div = bf.find('div', class_ = 'article')
        content = div.find('div', class_ = 'content')
        return content.getText()

if __name__ == '__main__':
    joke = getJoke()
    text = re.sub('\s', '', joke.getText()) # 去除空白
    itchat.auto_login(hotReload=True)

    # 获取用户名
    user = itchat.search_friends(name = '主淫')
    itchat.send(text, toUserName=user[0]['UserName'])