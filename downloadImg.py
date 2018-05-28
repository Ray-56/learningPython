# -*- coding:UTF-8 -*-
import requests, json, time, sys
from contextlib import closing

class get_photos(object):

    def __init__(self):
        self.photos_id = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
        self.target = 'http://unsplash.com/napi/feeds/home'
        self.cookies = {
            'uuid': '3256bb90-5fbe-11e8-98ab-bd1ddae1b03a',
            'xpos': '%7B%7D',
            '_ga': 'GA1.2.132661198.1527213113',
            '_gid': 'GA1.2.368125917.1527213113',
            '_sp_ses.0295': '*',
            '_sp_id.0295': 'da843bf9-a38b-4ff8-94e8-3110781bbbc6.1527213113.2.1527216177.1527213607.15c256fc-428e-446e-911c-30f54e63988c'
        }

    """
    函数说明:获取图片ID
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-05-25
    """
    def get_ids(self):
        req = requests.get(url=self.target, cookies=self.cookies, verify=False)
        html = json.loads(req.text)
        next_page = html['next_page']
        for each in html['photos']:
            self.photos_id.append(each['id'])
        time.sleep(1)

    """
    函数说明:图片下载
    Parameters:
        无
    Returns:
        无
    Modify:
        2018-05-25
    """
    def download(self, photo_id, filename):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        target = self.download_server.replace('xxx', photo_id)
        with closing(requests.get(url=target, stream=True, verify = False, cookies=self.cookies)) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size = 1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()

if __name__ == '__main__':
    gp = get_photos()
    print('获取图片连接中:')
    gp.get_ids()
    print(gp.photos_id)
    
    print('图片下载中:')
    for i in range(len(gp.photos_id)):
        print('  正在下载第%d张图片' % (i+1))
        gp.download(gp.photos_id[i], (i+1))