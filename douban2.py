""" 
伪装浏览器

需要登录的网站, 如果不是浏览器发送的请求, 则得不到响应.
所以, 我们需要将爬虫程序发出的请求伪装成浏览器正规军.
具体实现: 自定义网页请求报头
 """

#  采用伪装浏览器的方式爬取豆瓣

import urllib.request

# 定义保存函数
def saveFile(data):
    path = 'C:\\Users\\i5-6600\\Desktop\\python\\douban.out' # 字符串中的\需要转义
    f = open(path, 'wb')
    f.write(data)
    f.close()

# 网址
url = 'https://www.douban.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'
}

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

# 爬取的内容保存在文件中
saveFile(data)

data = data.decode('utf-8')

# 打印抓取的内容
print(data)

# 打印其它内容
print(type(res))
print(res.geturl())
print(res.info())
print(res.getcode())
