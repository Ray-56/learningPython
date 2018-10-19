from selenium import webdriver
from time import sleep
import unittest

class LoginCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()

    """ def login(self, userName, password):
        self.openPage(self.loginPageUrl)
        self.dr.implicitlyWait(5)
        self.dr.type('account', userName)
        self.dr.type('password', password)
        self.dr.click('submit') """

    # 定义登录方法
    def login(self, username, password):
        self.dr.get("http://localhost:8089/#/login")
        """ self.dr.find_elements_by_class_name("login-input-box")[0].find_element_by_tag_name('input').send_keys(username)
        self.dr.find_elements_by_class_name("login-input-box")[1].find_element_by_tag_name('input').send_keys(password)
        self.dr.find_element_by_css_selector("[class='login-form login']").find_element_by_class_name('el-button--primary').click() """
        self.getElement('s,.userMobile input').send_keys(username)

    def getElement(self, selector):
        if ',' not in selector:
            return self.dr.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == 'i' or selector_by == 'id':
            element = self.dr.find_element_by_id(selector_value)
        elif selector_by == 'n' or selector_by == 'name':
            element = self.dr.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.dr.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.dr.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.dr.find_element_by_partial_link_text(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.dr.find_element_by_tag_name(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            element = self.dr.find_element_by_xpath(selector_value)
        elif selector_by == 's' or selecotr_by == 'selector_selector':
            element = self.dr.find_element_by_css_selector(selector_value)
        else:
            raise NameError('Please enter a valid type of targeting elements (请输入有效的目标元素类型)')

        return element

    def type(self, selector, text):
        el = self.getElement(selector)
        el.clear()
        el.send_keys(text)

    def test_login_success(self):
        """ 用户名、密码正确 """
        self.login('13601973055', '123456') # 正确的用户名和密码
        sleep(3)

    """ def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit() """

if __name__ == '__main__':
    unittest.main()



