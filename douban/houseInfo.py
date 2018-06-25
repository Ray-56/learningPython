# -*- coding:UTF-8 -*-

import requests, json, sys, re, time, math   
from bs4 import BeautifulSoup
from urllib import parse

"""
类说明: 查询豆瓣租房信息  注意 不要被封了ip哟
Parameters:
    无
Returns:
    无
Modify:
    2018-05-30
"""
class HouseInfo(object):

    def __init__(self):
        self.target = 'https://www.douban.com/group/search?cat=1019&q=上海租房'
        self.cookies = {
            '__utma': '30149280.678446719.1507628080.1527733989.1527739128.16',
            '__utmb': '30149280.11.10.1527739128',
            '__utmc': '30149280',
            '__utmv': '30149280.15932',
            '__utmz': '30149280.1527651796.10.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            '__yadk_uid': 'FzB97hWmspDLV3Y2OMrfpaDq5dvRSwQN',
            '_pk_id.100001.8cb4': '9f3b50636b2779db.1507628080.13.1527739703.1527735960.',
            '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1527739127%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
            '_pk_ses.100001.8cb4': '*',
            '_vwo_uuid_v2': 'D01A720252ED5DEDCA4DF03885722F11D|f30ce68d9caac683e7214532254ea13c',
            'bid': 'RXHnBc2NN5I',
            'ck': '2wmS',
            'ct': 'y',
            'dbcl2': '"159324278:ncyDN2Xarqg"',
            'gr_user_id': '00be5d9b-454a-40d4-9bfc-d277ec0e0c5f',
            'll': '"108296"',
            'ps': 'y',
            'push_doumail_num': '0',
            'push_noty_num': '0',
            'viewed': '"6805117_27615777"',
        }
        self.proxies = {'http': '202.121.178.244:8080'} # requests ip伪装
        self.groups = [] # 所有小组
        self.groupNums = 0 # 小组数量
        self.searchKeyword = '整租三室' # 搜索关键词
        
        self.startTime = '2018-05-10'
        self.startTimeStamp = self.__getTimeStamp(self.startTime)
        self.searchTargets = [] # 所有小组 搜索关键词后的链接
        self.result = [] # 最终结果

    # 获取时间戳
    def __getTimeStamp(self, date, format = "%Y-%m-%d"):\
        # 将其转换为时间数组
        timeArray = time.strptime(date, format)
        # 转换为时间戳:
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    # 获取小组
    def getGroups(self):
        req = requests.get(url=self.target, cookies=self.cookies, verify=True)
        html = req.text
        print(req)
        bf = BeautifulSoup(html, 'html.parser')
        groups = bf.find('div', class_ = 'groups')
        a = groups.find_all('a', class_ = 'nbg')
        self.groupNums = len(a)
        for each in a:
            self.groups.append(each.get('href'))

    # 各小组的查询搜索关键词(searchKeyword)的结果
    def getSearchTarget(self, target):
        req = requests.get(url = target, cookies=self.cookies, verify=True)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        search = bf.find('div', class_ = 'group-topic-search')
        """ print(search.find('input', attrs={"name": "group"}).get('value'))
        # 这里会有一点问题 如果没有登录 有些小组进入到登录页 则没有获取到search 
        if search: """ 
        group = search.find('input', attrs={"name": "group"}).get('value')
        cat = search.find('input', attrs={"name": "cat"}).get('value')
        self.searchTargets.append('https://www.douban.com/group/search?group=%s&cat=%s&q=%s' %(group, cat, self.searchKeyword))

        time.sleep(1)

    # 小组中每页数据
    def getPageSource(self, target):
        req = requests.get(url = target, cookies=self.cookies, verify=True)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        pl = bf.find_all('tr', class_ = 'pl')
        
        for each in pl:
            a = each.find('td', class_ = 'td-subject').find('a')
            title = a.get('title')
            url = a.get('href')
            date = each.find('td', class_ = 'td-time').get('title')
            timeStamp = self.__getTimeStamp(date, format = '%Y-%m-%d %H:%M:%S')
            if timeStamp > self.startTimeStamp:
                item = {
                    'title': title,
                    'url': url,
                    'date': date
                }
                self.result.append(item)
                self.writer(title, '符合条件的房子.txt', '网址: %s ; 日期: %s;' %(url, date))
                
        time.sleep(1)

    # 获取
    def getGroupTitle(self, target):
        req = requests.get(url = target, cookies=self.cookies, verify=True)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        paginator = bf.find('div', class_ = 'paginator')
        pageSize = 50
        paginator_last = paginator.find('span', class_ = 'thispage').get('data-total-page')
        countText = paginator.find('span', class_ = 'count').getText() # eg: (共41460个结果)
        totalCount = int(re.findall(r'共([^个]+)', countText)[0]) # 取出总数量
        totalPage = math.ceil(totalCount / pageSize) # 计算总页数
        param = parse.parse_qs(target.split('?')[1]) # 获取url中参数集合
        group = param['group'][0]
        cat = param['cat'][0]
        q = param['q'][0]

        for i in range(totalPage):
            # print('小组%s 第%s页' %(group, i))
            sys.stdout.write(' 已下载:%.3f%%' % float(i/totalPage) + '\r')
            sys.stdout.flush()
            url = 'https://www.douban.com/group/search?start=%s&group=%s&cat=%s&q=%s' %(i * 50, group, cat, q)
            self.getPageSource(url)
            

        time.sleep(1)

    # 将爬到的数据 写入文件
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name +'\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    hi = HouseInfo()
    hi.getGroups()
    # for i in range(hi.groupNums): 
    for i in range(1): # 现在只爬第一个小组内容
        hi.getSearchTarget(hi.groups[i])
    for i in range(1): # 现在只爬第一个小组搜索整租后的
        hi.getGroupTitle(hi.searchTargets[i])
    # print(hi.result) # 爬到的json数据
    print('完成')
