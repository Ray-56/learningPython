#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'fgk'

'''
异步web应用
'''

import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

import orm

from models import User

def test(loop):
    yield from orm.create_pool(loop=loop, host='localhost',port=3306, user='root', password='123456', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
    

def index(request):
    return web.Response(body = b'<h1>hello world</h1>', content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()