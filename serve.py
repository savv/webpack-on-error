#!/usr/bin/env python3

from aiohttp import web

app = web.Application()
app.router.add_static('/', './')
app.router.add_static('/dist', './dist')
web.run_app(app, port=8000)
