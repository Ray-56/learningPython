# -*- coding:UTF-8 -*-

import requests

"""
说明: ip伪装
Modify:
    2018-05-31
"""

url = "http://www.baidu.com"
proxies = {
  "http": "122.114.31.177:808",
  "http": "61.135.217.7:80"
}
response = requests.get(url, proxies=proxies)
print(response)