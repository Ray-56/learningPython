# -*- coding: utf-8 -*-

__author__ = 'Fgk'

import unittest
from time import sleep

from public.common.automate_driver import AutomateDriver
from public.pages.sub_page import SubPage
from public.common.log import Log

""" 
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例方法以 test 开头
4. 考虑使用 setUp() 和 tearDown()
"""

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """  
        开始当前所有测试前的准备事项
        :return:
        """
        self.dr = AutomateDriver()
        self.logger = Log()
        self.logger.warning('############################### START ###############################')
        self.baseUrl = 'http://localhost:8089'
        self.loginPage = SubPage(self.dr, self.baseUrl)

    def setUp(self):
        """  
        开始每个测试前的准备事项
        :return:
        """
        print('setUp')
        # self.dr = AutomateDriver()
        # self.baseUrl = 'http://localhost:8089'
        # self.loginPage = SubPage(self.dr, self.baseUrl)
        
    @classmethod
    def tearDownClass(self):
        """  
        结束每个测试后的清理工作
        :return:
        """
        pass
        self.dr.quitBrowser()

    # def test_login_success(self):
    #     """  
    #     测试用例: 登录 用户名、密码正确
    #     """
    #     # 利用页面对象进行登录
    #     self.loginPage.login('13601973055', '123456')
    #     self.dr.implicitlyWait(5)

    #     companies = self.dr.getElements('s,.card-box li')

    #     # 判断公司长度 长度大于1则默认选择第一个企业
    #     if len(companies) > 1: 
    #         companies[0].click()
    #     sleep(1)

    #     msg = self.dr.getText('s,.el-message p')
        
    #     self.assertTrue('登录成功' in msg) #用assertTrue(x)方法来断言  bool(x) is True 登录成功后 登陆成功消息在msg中

    def test_login_pwd_error(self):
        """ 
        测试用例: 用户名正确 密码不正确 
        """
        self.loginPage.login('13601973055', '1234567') # 用户名正确 密码错误
        sleep(1)

        msg = self.dr.getText('s,.el-message p')

        self.assertIn('用户名或密码不正确', msg)   #用assertIn(a,b)方法来断言 a in b  '用户名或密码不正确'在error_message里

    def test_login_pwd_null(self):
        """ 
        测试用例: 用户名正确 密码为空 
        """
        sleep(5)
        self.loginPage.login('13601973055', '') # 用户名正确 密码为空
        sleep(1)

        err_msg = self.dr.getText('s,.userPwd+.el-form-item__error')

        self.assertEqual(err_msg, '请输入密码')  #用assertEqual(a,b)方法来断言  a == b  '请输入密码' 等于 err_msg

    # def test_login_user_error(self):
    #     """ 
    #     测试用例: 用户名错误 密码正确 
    #     """
    #     self.loginPage.login('136019730551', '123456') # 用户名错误 密码正确
    #     sleep(1)

    #     msg = self.dr.getText('s,.el-message p')

    #     self.assertIn('用户名或密码不正确', msg)   #用assertIn(a,b)方法来断言 a in b  '用户名或密码不正确'在error_message里

    # def test_login_user_null(self):
    #     """ 
    #     测试用例: 用户名为空 密码正确 
    #     """
    #     self.loginPage.login('', '123456') # 用户名为空 密码正确
    #     sleep(1)

    #     err_msg = self.dr.getText('s,.userMobile+.el-form-item__error')

    #     self.assertEqual(err_msg, '请输入手机号')  #用assertEqual(a,b)方法来断言  a == b  '请输入手机号' 等于 err_msg