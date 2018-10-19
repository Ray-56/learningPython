# -*- coding: utf-8 -*-

__author__ = 'Fgk'

class BasePage():

    def __init__(self, driver, baseUrl):
        """  
        构造方法
        :param driver: 封装好的webdriver
        :param baseUrl: 系统的基本url http://localhost:8089
        """
        self.baseUrl = baseUrl
        self.dr = driver

    def openPage(self, url):
        """  
        打开系统页面, 通过凭借URL的方式
        :param url: /login
        :return:
        """
        self.dr.navigate(self.baseUrl + '/#' + url)