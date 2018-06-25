#cookie登陆获取
import requests
from urllib import parse
url='https://www.douban.com/accounts/login'
data={'username':'18217023823',
      'password':'asdfasdf', # poiuy0987...
      'source':'index_nav',}
url_data = parse.urlencode(data)
session = requests.session()
rq = session.post(url, data)
for i in session.cookies:
    print(i.name)
    print(i.value)
# 利用session节点进行登陆后的网站测试
""" rq1=session.get('https://www.douban.com/group/search?cat=1019&q=上海租房')
print(rq1.text) """