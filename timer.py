# -*- coding:UTF-8 -*-

"""
类说明: 定时执行程序
Parameters:
    无
Returns:
    无
Modify:
    2018-05-28
"""

import schedule, time

def job(text):
    print("I'm working...", text)

schedule.every(1).minutes.do(job, '1') # 每一分钟执行一次
schedule.every().hour.do(job, '2') # 每一小时执行一次
schedule.every().day.at("10:41").do(job, '3') # 每天10:41执行一次
schedule.every().monday.do(job, '4') # 每周一执行一次
schedule.every().wednesday.at("13:15").do(job, '5') # 每周三13:15执行一次
 
while True:
    schedule.run_pending()
    time.sleep(1)