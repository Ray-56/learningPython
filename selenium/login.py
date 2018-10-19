from selenium import webdriver
from time import sleep
import unittest

class LoginCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get("http://localhost:8089/#/login")
        self.dr.find_elements_by_class_name("login-input-box")[0].find_element_by_tag_name('input').send_keys(username)
        self.dr.find_elements_by_class_name("login-input-box")[1].find_element_by_tag_name('input').send_keys(password)
        self.dr.find_element_by_css_selector("[class='login-form login']").find_element_by_class_name('el-button--primary').click()

    def test_login_success(self):
        """ 用户名、密码正确 """
        self.login('13601973055', '123456') # 正确的用户名和密码
        self.dr.implicitly_wait(2)
        companies = self.dr.find_element_by_class_name('card-box').find_elements_by_tag_name('li')
        if len(companies) > 1: # 判断公司长度 长度大于1则
            companies[0].click()
        self.dr.implicitly_wait(2)
        msg = self.dr.find_element_by_class_name('el-message').find_element_by_tag_name('p')
        self.assertTrue('登录成功' in msg.text)   #用assertTrue(x)方法来断言  bool(x) is True 登录成功后 登陆成功消息在msg中
        self.dr.get_screenshot_as_file("C:\\Users\\i5-6600\\Documents\\learningPython\\selenium\\img\\login_success.png")  #截图  可自定义截图后的保存位置和图片命名

    def test_login_pwd_error(self):
        """ 用户名正确 密码不正确 """
        self.login('13601973055', '1234567') # 用户名正确 密码错误
        sleep(1)
        msg = self.dr.find_element_by_class_name('el-message').find_element_by_tag_name('p')
        self.assertIn('用户名或密码不正确', msg.text)   #用assertIn(a,b)方法来断言 a in b  '用户名或密码不正确'在error_message里
        self.dr.get_screenshot_as_file("C:\\Users\\i5-6600\\Documents\\learningPython\\selenium\\img\\login_pwd_error.png") 

    def test_login_pwd_null(self):
        """ 用户名正确 密码为空 """
        self.login('13601973055', '') # 用户名正确 密码为空
        sleep(1)
        err_msg = self.dr.find_element_by_css_selector(".userPwd+.el-form-item__error").text # 用CSS选择器查找元素
        sleep(1)
        self.assertEqual(err_msg, '请输入密码')  #用assertEqual(a,b)方法来断言  a == b  '请输入密码' 等于 err_msg
        self.dr.get_screenshot_as_file("C:\\Users\\i5-6600\\Documents\\learningPython\\selenium\\img\\login_pwd_null.png")

    def test_login_user_error(self):
        """ 用户名错误 密码正确 """
        self.login('136019730551', '123456') # 用户名错误 密码正确
        sleep(1)
        msg = self.dr.find_element_by_class_name('el-message').find_element_by_tag_name('p').text
        self.assertIn('用户名或密码不正确', msg)   #用assertIn(a,b)方法来断言 a in b  '用户名或密码不正确'在error_message里
        self.dr.get_screenshot_as_file("C:\\Users\\i5-6600\\Documents\\learningPython\\selenium\\img\\login_user_error.png") 

    def test_login_user_null(self):
        """ 用户名为空 密码正确 """
        self.login('', '123456') # 用户名为空 密码正确
        err_msg = self.dr.find_element_by_css_selector(".userMobile+.el-form-item__error").text # 用CSS选择器查找元素
        self.assertEqual(err_msg, '请输入手机号')  #用assertEqual(a,b)方法来断言  a == b  '请输入手机号' 等于 err_msg
        self.dr.get_screenshot_as_file("C:\\Users\\i5-6600\\Documents\\learningPython\\selenium\\img\\login_user_null.png")

    """ def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit() """

if __name__ == '__main__':
    unittest.main()