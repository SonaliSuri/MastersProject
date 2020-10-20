import asyncio
from aiohttp import web
from aiohttp import ClientSession
import requests
import constant as const
import time


host = 'localhost'
port = '8049'
counter = 0


def get_reply(response):
    print("getreply")
    global counter
    counter += 1
    print('Number of reply messages received:', counter)
    if counter == 3:
        print("SPBFT Comppleted")
        # paxos = "http://0.0.0.0:1050/propose"
        # response = requests.get(url=paxos)
    return web.Response(text="My message")


app = web.Application()
app.router.add_route('POST', '/get_reply/', get_reply)
loop = asyncio.get_event_loop()
handler = app.make_handler()
f = loop.create_server(handler, const.host, const.port)
srv = loop.run_until_complete(f)
print('serving on', srv.sockets[0].getsockname())


try:
    loop.run_forever()

except KeyboardInterrupt:
    pass
finally:
    srv.close()
    loop.run_until_complete(srv.wait_closed())
    loop.run_until_complete(handler.finish_connections(1.0))
    loop.run_until_complete(app.finish())
loop.close()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(initiate_pbft("http://"+const.host_1+':'+const.port_1+'/prep/'))
