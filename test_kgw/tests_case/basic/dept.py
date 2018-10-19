# -*- coding: utf-8 -*-

__author__ = 'Fgk'

import unittest
from time import sleep

from core.automate_driver import AutomateDriver
from sub_page import SubPage

""" 
1. 导入 unittest
2. 继承 unittest.TestCase
3. 写用例方法以 test 开头
4. 考虑使用 setUp() 和 tearDown()
"""

class DeptTests(unittest.TestCase):
    def setUp(self):
        """  
        开始每个测试前的准备事项
        :return:
        """
        self.dr = AutomateDriver()
        self.baseUrl = 'http://localhost:8089'

    def tearDown(self):
        """  
        结束每个测试后的清理工作
        :return:
        """
        self.dr.quitBrowser()

    def test_basic_dept(self):
        """  
        测试用例: 基础资料 部门资料
        :return:
        """
        # 新建页面对象
        deptPage = SubPage(self.dr, self.baseUrl)
        self.dr.implicitlyWait(5)

        # 利用页面对象打开部门资料页面
        deptPage.dept()
        sleep(3)

        # 点击添加按钮
        self.dr.click('c,kgw-btn-addAll')

        # 表格第一行中输入
        # self.dr.getElement('s,.el-table__body-wrapper .el-table__row:first-child [test-data=deptSerial] input').send_keys('你好 你好')
        # self.dr.getElement('s,.el-table__body-wrapper .el-table__row:first-child [test-data=deptName] input').send_keys('无名的部门')
        self.dr.type('s,.el-table__body-wrapper .el-table__row:first-child [test-data=deptSerial] input', '你好 你好')
        self.dr.type('s,.el-table__body-wrapper .el-table__row:first-child [test-data=deptName] input', '无名的部门')

        # 上级部门下拉框触发
        self.dr.click('s,.el-table__body-wrapper .el-table__row:first-child [test-data=parentName] .el-select input')
        sleep(0.3)
        # 上级部门下拉框选择
        self.dr.getElement('s,body>.el-select-dropdown .el-select-dropdown__list').find_elements_by_class_name('el-select-dropdown__item')[0].click()

        # 点击保存
        self.dr.click('s,#app-content>header button:first-child')
        sleep(0.5)

        msg = self.dr.getText('s,.el-message p')
        
        self.assertEqual(msg, '保存成功')

    def test_basic_dept_add_required(self):
        """ 
        测试用例: 新增必填项未填 
        """
        pass

