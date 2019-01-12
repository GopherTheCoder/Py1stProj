import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

def when(request):
    now = time.strftime("%H:%M:%S", time.localtime())
    return web.Response(body=now, content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)     #创建router来处理浏览器请求
    app.router.add_route('GET', '/when', when)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
#协程
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()