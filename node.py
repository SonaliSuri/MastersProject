import asyncio
from aiohttp import web
from aiohttp import ClientSession
import requests

"""
['ATTRS', 'POST_METHODS', '_MutableMapping__marker', '__abstractmethods__', '__bool__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '$
"""

import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2
from aiohttp import ClientResponse
import constant as const
from pathlib import Path
import time
import json


class Node:

    def __init__(self, host, port, to_host=None, to_port=None, viewnum=""):
        print("Hello")
        self.host = host
        self.port = port
        self.to_host = to_host
        self.to_port = to_port
        self.view_num = viewnum
        const.host_node = host
        const.port_node = port
        app = web.Application(client_max_size=41300 * 2 ** 10)

        app.router.add_route('POST', '/prep/', self.prepare)
        app.router.add_route('POST', '/commit_ack/', self.commit_ack)



        loop = asyncio.get_event_loop()
        handler = app.make_handler()
        f = loop.create_server(handler, const.host_node, const.port_node)
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
        print(const.host_node, const.port_node)

    def next_commit_ack(self, params, json_data):
        print("Reply phase started:", time.time())
        url_client = "http://" + const.host + ':' + const.port + '/get_reply/'
        requests.post(url=url_client, headers=params, json=json_data)
        print("Reply phase ended:", time.time())
        if self.to_host is not None and self.to_port is not None:
            url = "http://" + self.to_host + ':' + self.to_port + '/commit_ack/'
            requests.post(url=url, headers=params, json=json_data)
        else:

            new_msg = [const.open_brac, params[const.VIEW], params[const.MSG_SEQ],
                       params[const.TYPE], params[const.MSG], const.close_brac]
            new_params = {
                      const.MSG: ", ".join(new_msg)
                      }
            print("Ended commit_ack:", time.time())
            #url_draw = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
            #requests.post(url=url_draw, headers=new_params)
            return

    def commit_ack(self, request):
        json_data = {}
        if self.view_num == "1":
            print("Started commit_ack", time.time())
            msg = [const.open_brac, request[const.VIEW], request[const.MSG_SEQ],
                   request[const.TYPE], request[const.MSG],
                   const.close_brac]
            params = {const.VIEW: "1",
                      const.MSG_SEQ: str(int(request[const.MSG_SEQ]) + 1),
                      const.TYPE: const.COMMITACK,
                      const.MSG: ", ".join(msg)
                      }
        else:

            msg = [const.open_brac, request.headers[const.VIEW], request.headers[const.MSG_SEQ],
                   request.headers[const.TYPE],
                   request.headers[const.MSG], const.close_brac]

            params = {const.VIEW: self.view_num,
                      const.MSG_SEQ: str(int(request.headers[const.MSG_SEQ]) + 1),
                      const.TYPE: const.COMMITACK,
                      const.MSG: ", ".join(msg)
                      }
        print("Node "+self.view_num+": ", params)
        #url_draw = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
        #requests.post(url=url_draw, headers=params)
        self.next_commit_ack(params, json_data)
        return web.Response(text="My message")

    def create_commit_msg(self, request):
        if self.view_num == "3":
            print("Commit Phase Started:", time.time())
        msg = [const.open_brac, request[const.VIEW], request[const.MSG_SEQ],
               request[const.TYPE],
               request[const.MSG], const.close_brac]
        params = {const.VIEW: self.view_num,
                  const.MSG_SEQ: str(int(request[const.MSG_SEQ]) + 1),
                  const.TYPE: const.COMMIT,
                  const.MSG: ", ".join(msg),
                  const.commit: str(int(request[const.commit])+1)
                  }
        #url_draw = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
        #requests.post(url=url_draw, headers=params)
        return params

    async def prepare(self, request):
        print("inside the prepare request")
        start_time = time.time()
        if self.view_num == "1":
            print("Prepare Phase started:", start_time)
            msg = [const.open_brac, request.headers[const.VIEW], request.headers[const.MSG_SEQ],
                   request.headers[const.TYPE], const.close_brac]

            # print("Commit", request.headers[const.commit])
            params = {const.VIEW: self.view_num,
                      const.MSG_SEQ: str(int(request.headers[const.MSG_SEQ]) + 1),
                      const.TYPE: const.PRE_PREPARE,
                      const.MSG: ", ".join(msg),
                      const.prep: str(int(request.headers[const.prep]) + 1),
                      const.commit: str(int(request.headers[const.commit]))
                      }
            json_data = await request.json()

        else:

            msg = [const.open_brac, request.headers[const.VIEW], request.headers[const.MSG_SEQ],
                   request.headers[const.TYPE], request.headers[const.MSG], const.close_brac]

            params = {const.VIEW: self.view_num,
                  const.MSG_SEQ: str(int(request.headers[const.MSG_SEQ]) + 1),
                  const.TYPE: const.PREPARE,
                  const.MSG: ", ".join(msg),
                  const.prep: str(int(request.headers[const.prep]) + 1),
                const.commit: str(int(request.headers[const.commit]))
                  }

            json_data = await request.json()

        # print(json_data)

        # url_diagram = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
        # result = requests.post(url=url_diagram, headers=params)

        # const.prep = const.prep + 1
        # print("Prep msg", params[const.prep])

        if self.to_port and self.to_host and int(params[const.prep]) < 2 * const.faulty:
            # print("Node: "+self.view_num+": ", params)
            url = "http://" + self.to_host + ':' + self.to_port + '/prep/'

            response = requests.post(url=url, headers=params, json=json_data)

            if self.view_num == "1":
                print("Prepare Phase Ended:", time.time())
            print("response.text) =", response)
            print("response.text) =", response.text)
            response_content = self.create_commit_msg(json.loads(response.text))
            if self.view_num == "1":
                print("Commit Phase ended at: ", time.time())
                response_content = self.commit_ack(response_content)
                print("Node: " + self.view_num + ": ", response_content)
                return web.Response(text="My message")
            else:
                response_content = json.dumps(response_content)

                print("Node: " + self.view_num + ": ", response_content)
                return web.Response(text=response_content)
        else:

            response_content = ""
            # url_diagram = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
            # result = requests.get(url=url_diagram, headers=params)
            # print(result)
            if int(params[const.commit]) < 2 * const.faulty + 1:
                response_content = self.create_commit_msg(params)
                response_content = json.dumps(response_content)
                print("Node  " + self.view_num + ": ", response_content)

            return web.Response(text=response_content)


class Drawings(Node):
    def __init__(self, host, port, viewnum=""):
        print("Hello")
        self.host = host
        self.port = port
        self.view_num = viewnum
        self.arr=[]
        const.host_node = host
        const.port_node = port
        app = web.Application(client_max_size=41300 * 2 ** 10)
        here = Path(__file__).resolve().parent
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(here)))

        app.router.add_route('POST', '/initiate/', self.initiating)
        #app.router.add_route('POST', '/change_text/', self.change_text)

        loop = asyncio.get_event_loop()
        handler = app.make_handler()
        f = loop.create_server(handler, const.host_node, const.port_node)
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
        print(const.host_node, const.port_node)

    @aiohttp_jinja2.template('display.html')
    async def change_text(self, request):

        print("````````````````````````change_text`````````````````````````", request.headers)
        if const.MSG in request.headers:
            msg = 'stage'+':'+str(request.headers[const.MSG])
            self.arr.append(msg)
            self.arr.append("\n")
            self.arr.append("================================================================")
            self.arr.append("\n")

            return {'stage': " ".join(self.arr)}
        else:

            return {'stage': " ".join(self.arr)}

        #return {'stage':  msg}


