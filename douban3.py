""" 
下载豆瓣首页图片

伪装成浏览器 爬取首页图片, 保存到指定文件
"""

# 导入所需要的库
import urllib.request, socket, re, sys, os

# 定义文件保存路径
targetPath = path = 'C:\\Users\\i5-6600\\Desktop\\python\\douban.out' # 字符串中的\需要转义

def saveFile(path):
    # 检测路径是否有效
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    # 设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos+1:])
    return t

# 用if __name__ == '__main__'来判断是否是在直接运行.py文件

# 网址
url = 'https://www.douban.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'
}

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):

    print(link)
    try:
        urllib.request.urlretrieve(link, saveFile(link))
    except:
        print('失败')