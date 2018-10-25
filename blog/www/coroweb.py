#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'fgk'

'''
封装 `aiohttp` 的web框架
'''

import asyncio, os, inspect, logging, functools

def get(path):
    '''
    Define decorator @get('/path'). 定义修饰符
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    pass

class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn

    @asyncio.coroutine
    def __call__(self, request):
        kw = None
        pass

