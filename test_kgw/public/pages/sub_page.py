# -*- coding: utf-8 -*-

__author__ = 'Fgk'

from public.pages.base_page import BasePage
from time import sleep

class SubPage(BasePage):
    def __init__(self, driver, baseUrl):
        """  
        :param driver:
        :param baseUrl:
        """

        # 调用其 基类 BasePage的 构造函数
        # 实现 基类 的构造函数功能
        super().__init__(driver, baseUrl)
        self.loginPageUrl = '/login'
        self.deptPageUrl = '/appContent/basic/Dept'
        self.dr.clearCookies()

    def login(self, userName, password):
        self.openPage(self.loginPageUrl)
        # self.dr.implicitlyWait(5)
        self.dr.type('s,.userMobile input', userName)
        self.dr.type('s,.userPwd input', password)
        self.dr.click("s,[class='login-form login'] .el-button--primary")

    def dept(self):
        self.login('13601973055', '123456')
        self.dr.implicitlyWait(10)

        companies = self.dr.getElements('s,.card-box li')

        # 判断公司长度 长度大于1则默认选择第一个企业
        if len(companies) > 1: 
            companies[0].click()
        sleep(1)

        self.openPage(self.deptPageUrl)

        
