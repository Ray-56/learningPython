from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
driver.get("http://localhost:8089/#/login")
# driver.get("http://yc.kuguanwang.com/v3-pc/")
driver.find_elements_by_class_name("login-input-box")[0].find_element_by_tag_name('input').send_keys("13601973055");

driver.find_elements_by_class_name("login-input-box")[1].find_element_by_tag_name('input').send_keys("123456");

driver.find_element_by_css_selector("[class='login-form login']").find_element_by_class_name('el-button--primary').click();

driver.implicitly_wait(3)

driver.find_element_by_class_name('card-box').find_elements_by_tag_name('li')[0].click()
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
time.sleep(3)
driver.close()