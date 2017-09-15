from aiohttp import web

app = web.Application()
app.router.add_static('/', './')
web.run_app(app, port=8000)
