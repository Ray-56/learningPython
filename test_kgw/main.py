# -*- coding: utf-8 -*-

__author__ = 'Fgk'

from public.common.tests_runner import TestRunner

if __name__ == '__main__':
    # 实例化一个runner
    runner = TestRunner()

    # 执行测试
    runner.runTest()

    # 发送测试结果
    # runner.sendEmail('1070524274@qq.com')