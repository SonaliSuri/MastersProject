from SPbft import Client
from SPbft import Node
from aiohttp import web
import aiohttp
import asyncio


# @routes.get('/')
async def hello(request):
    global count
    if count ==0:
        print("in hello", count)
        r4 = Node(None, 4, 4)
        r3 = Node(r4, 3, 3)
        r2 = Node(r3, 2, 2)
        r1 = Node(r2, 1, 1, True)
        c1 = Client(r1)
        count+=1
        return c1.init_pre_prepare(r1, c1)
    else:
        exit(0)


async def initiate(request):
    async with aiohttp.ClientSession() as session:
        print("in main")
        response = await fetch(session, 'http://0.0.0.0:8080/')
        print(response)

    pass


async def preprepare(request):
    pass


async def prepare(request):
    pass


async def commit(request):
    pass


async def committed(request):
    pass


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        print("in main")



count = 0
#routes = [web.get('/', hello)]
#print("routes",  routes)
app = web.Application()
app.add_routes([
    web.get('/', hello)
    ])

web.run_app(app, host='localhost', port='8080', access_log=None)
