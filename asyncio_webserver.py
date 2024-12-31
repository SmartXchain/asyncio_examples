from aiohttp import web

async def handle(request):
    return web.Response(text="Hello, asyncio!")

app = web.Application()
app.add_routes([web.get('/', handle)])

web.run_app(app)