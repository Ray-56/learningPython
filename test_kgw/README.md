## PY UI自动化测试 ##
< python3.0 + selenium 
### 项目结构 ###
```
-test_kgw
    |-config 配置文件目录
        |-config.ini 存放配置文件
        |-global_params.py 重要的全局参数, 如log、report的路径配置等
    |-data 测试数据
        |-uat 正式环境测试数据
        |-dev 测试环境测试数据
            |-test.xlsx 某个测试的表格数据 
    |-public 公共的文件库
        |-common 封装的公共方法
            |-send_mail.py 发送邮件
            |-test_runner.py 启动测试
            |-automate_driver.py 封装webdriver方法 
            |-HTMLTestRunner.py 生成html测试报告插件 3.0版本
        |-pages 使用pageobject模式编写测试脚本，存放page的目录
            |-base_page.py 基础配置
            |-sub_page.py 页面配置
    |-report 测试报告
        |-image 截图目录
        |-log 日志
            |-2018-7-19.log
        |-html 测试报告页面
            |-result.html 测试报告
    |-tests_case 存放测试用例
        |-basic 所有基础资料
            |-dept.py 部门资料
        |-login.py 登录
    |-README.md 说明文档
    |-main.go 程序执行入口
```
### 功能点 ###

### 前景提要 ##
欲学此功 必先掌握:
+ python3.0 
+ selenium
+ git(sourceTree)

### 问题记录 ###
__在用HTMLTestRunner时__
HTMLTestRunne作者是基于py2.0版本写的, 如果3.0要使用需要修改部分代码 这里不做赘述
在测试用例用```test_case```中使用```setUpClass```以及```tearDownClass```方法时:
```python
@classmethod
def setUpClass(self):
    # do something
    pass

@classmethod
def tearDownClass(self):
    # do something
    pass
```
如不加```@classmethod```则会报错:
```
Traceback (most recent call last):
  File "C:\Users\i5-6600\AppData\Local\Programs\Python\Python36\lib\unittest\suite.py", line 163, in _handleClassSetUp
    setUpClass()
TypeError: setUpClass() missing 1 required positional argument: 'self'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "main.py", line 12, in <module>
    runner.runTest()
  File "C:\Users\i5-6600\Documents\learningPython\test_kgw\tests_runner.py", line 40, in runTest
    runner.run(suite)
  File "C:\Users\i5-6600\Documents\learningPython\test_kgw\core\HTMLTestRunner.py", line 628, in run
    test(result)
  File "C:\Users\i5-6600\AppData\Local\Programs\Python\Python36\lib\unittest\suite.py", line 84, in __call__
    return self.run(*args, **kwds)
  File "C:\Users\i5-6600\AppData\Local\Programs\Python\Python36\lib\unittest\suite.py", line 122, in run
    test(result)
  File "C:\Users\i5-6600\AppData\Local\Programs\Python\Python36\lib\unittest\suite.py", line 84, in __call__
    return self.run(*args, **kwds)
  File "C:\Users\i5-6600\AppData\Local\Programs\Python\Python36\lib\unittest\suite.py", line 114, in run
    self._handleClassSetUp(test, result)
  File "C:\Users\i5-6600\AppData\Local\Programs\Python\Python36\lib\unittest\suite.py", line 170, in _handleClassSetUp
    self._addClassOrModuleLevelException(result, e, errorName)
  File "C:\Users\i5-6600\AppData\Local\Programs\Python\Python36\lib\unittest\suite.py", line 216, in _addClassOrModuleLevelException
    result.addError(error, sys.exc_info())
  File "C:\Users\i5-6600\Documents\learningPython\test_kgw\core\HTMLTestRunner.py", line 584, in addError
    output = self.complete_output()
  File "C:\Users\i5-6600\Documents\learningPython\test_kgw\core\HTMLTestRunner.py", line 558, in complete_output
    return self.outputBuffer.getvalue()
AttributeError: '_TestResult' object has no attribute 'outputBuffer'
```