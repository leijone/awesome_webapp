__author__ = 'ray'
'''
async web application
'''
import logging;

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


# 如果返回的结果是有IO耗时操作的,可以使用协程,如果不是,可以去掉async,直接返回一个函数
def index(request):
    # 数据传输和保存需要指定编码,一般为utf-8格式,读取的内存中就成unicode编码了,content_type来指定传输的数据的类型,这里是网页
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    # 创建一个web服务器对象
    app = web.Application(loop=loop)
    # 通过router的指定的方法可以把请求的链接和对应的处理函数关联在一起
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', '9000')
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
