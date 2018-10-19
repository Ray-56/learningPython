# -*- coding: utf-8 -*-

__author__ = 'Fgk'

from selenium import webdriver
from selenium.webdriver.support.select import Select

class AutomateDriver(object):
    """
    a simple demo of selenium framework tool
    一个简单的selenium框架工具演示 
    """

    def __init__(self):
        driver = webdriver.Chrome()
        try:
            self.dr = driver
        except Exception:
            raise NameError('Chrome 插件没有找到')

    def clearCookies(self):
        """ 
        驱动程序初始化后清除所有cookie
        """
        self.dr.delete_all_cookies()

    def refreshBrowser(self):
        self.dr.refresh()

    def maximizeWindow(self):
        self.dr.maximize_window()

    def navigate(self, url):
        self.dr.get(url)

    def quitBrowser(self):
        self.dr.quit()

    def closeBrowser(self):
        self.dr.close()

    def getElements(self, selector):
        if ',' not in selector:
            return self.dr.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "s" or selector_by == 'selector_selector':
            element = self.dr.find_elements_by_css_selector(selector_value)

        return element

    def getElement(self, selector):
        """
        按照选择器定位元素
        :arg
        选择器应该按照 'i,xxx' 样子传递 
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        if ',' not in selector:
            return self.dr.find_element_by_id(selector)
        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if selector_by == "i" or selector_by == 'id':
            element = self.dr.find_element_by_id(selector_value)
        elif selector_by == "n" or selector_by == 'name':
            element = self.dr.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.dr.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.dr.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.dr.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.dr.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            element = self.dr.find_element_by_xpath(selector_value)
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.dr.find_element_by_css_selector(selector_value)
        else:
            raise NameError('请输入有效的定位元素类型')

        return element

    def type(self, selector, text):
        """ 
        操作输入框

        用法:
        dr.type('i,el', '要输入的文字')
        """

        el = self.getElement(selector)
        # el.clear()
        el.send_keys(text)

    def click(self, selector):
        """ 
        它可以单击任何可以单击的 文本/图像(text / image)
        Connection, check box, radio buttons, and even drop-down box etc..
        (连接，复选框，单选按钮，甚至下拉框等)

        Usage:
        dr.click('i,el')
        """
        el = self.getElement(selector)
        el.click()

    def selectByIndex(self, selector, index):
        """ 
        it can click any text / image can be clicked
        connection, check box, radio buttons, and event drop-down box etc...

        Usage:
        dr.select_by_index('i,el')
        """
        el = self.getElement(selector)
        Select(el).select_by_index(index)

    def clickByText(self, text):
        """ 
        Click the element by the link text

        Usage:
        dr.click_text('新闻')
        """
        self.getElement('p,' + text).click()

    def submit(self, selector):
        """
        Submit the specified from.

        Usage:
        dr.submit('i,el') 
        """
        el = self.getElement(selector)
        el.submit()

    def executeJs(self, script):
        """ 
        Execute JavaScript scripts. 执行js脚本

        Usage:
        dr.js('window.scrollTo(200, 1000);')
        """
        self.dr.execute_script(script)

    def getAttribute(self, selector, attribute):
        """  
        Gets the value of an element attribute.

        Usage:
        dr.get_attribute('i,el', 'type')
        """
        el = self.getElement(selector)
        return el.getAttribute(attribute)

    def getText(self, selector):
        """  
        Get element text information

        Usage:
        dr.get_text('i,el')
        """
        el = self.getElement(selector)
        return el.text

    def getDisplay(self, selector):
        """  
        Gets the element to display, The return result is true or false.

        Usage:
        dr.get_display('i,el')
        """
        el = self.getElement(selector)
        return el.is_displayed()

    def getTitle(self):
        """  
        get window title.

        Usage:
        dr.get_title()
        """
        return self.dr.title

    def getUrl(self):
        """  
        Get the URL address of the current page.

        Usage:
        dr.get_url()
        """
        return self.dr.current_url

    def acceptAlert(self):
        """  
        Accept warning box.

        Usage:
        dr.accept_alert()
        """
        self.dr.switch_to.alert.accept()

    def dismissAlert(self):
        """  
        Dismisses the alert available. 驳回可用的alert

        Usage:
        dr.dismissAlert()
        """
        self.dr.switch_to.alert.dismiss()

    def implicitlyWait(self, secs):
        """ 
        Implicitly wait. All elements on the page. 隐式等待

        Usage:
        dr.implicitly_wait(10)
        """
        self.dr.implicitly_wait(secs)

    def switchFrame(self, selector):
        """  
        Switch to the specified frame. 切换到指定的帧

        Usage:
        dr.switch_to_frame('i,el')
        """
        el = self.getElement(selector)
        self.dr.switch_to.frame(el)

    def switchDefaultFrame(self):
        """ 
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        dr.switch_to_frame_out()
        """
        self.dr.switch_to.default_content()

    def openNewWindow(self, selector):
        """  
        Open the new window and switch the handle to the newly opened window.

        Usage:
        dr.open_new_window()
        """
        original_window = self.dr.current_window_handle
        el = self.getElement(selector)
        el.click()
        all_handles = self.dr.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.dr._switch_to.window(handle)

