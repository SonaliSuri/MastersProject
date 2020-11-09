import asyncio
from aiohttp import web
from aiohttp import ClientSession
import requests

"""
['ATTRS', 'POST_METHODS', '_MutableMapping__marker', '__abstractmethods__', '__bool__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__orig_bases__', '__parameters__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_cache', '_client_max_size', '_content_dict', '_content_type', '_headers', '_http_date', '_loop', '_match_info', '_message', '_method', '_parse_content_type', '_payload', '_payload_writer', '_post', '_prepare_hook', '_protocol', '_read_bytes', '_rel_url', '_state', '_stored_content_type', '_task', '_transport_peername', '_transport_sslcontext', '_version', 'app', 'body_exists', 'can_read_body', 'charset', 'clear', 'clone', 'config_dict', 'content', 'content_length', 'content_type', 'cookies', 'forwarded', 'get', 'has_body', 'headers', 'host', 'http_range', 'if_modified_since', 'if_range', 'if_unmodified_since', 'items', 'json', 'keep_alive', 'keys', 'loop', 'match_info', 'message', 'method', 'multipart', 'path', 'path_qs', 'pop', 'popitem', 'post', 'protocol', 'query', 'query_string', 'raw_headers', 'raw_path', 'read', 'rel_url', 'release', 'remote', 'scheme', 'secure', 'setdefault', 'task', 'text', 'transport', 'update', 'url', 'values', 'version', 'writer']
"""

from aiohttp import ClientResponse
from aiohttp import web
import constant as const
from pathlib import Path
import aiohttp_jinja2
import asyncio
import jinja2
import json
import time


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
        app = web.Application()

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

    def next_commit_ack(self, params):
        print("Reply phase started:", time.time())
        url_client = "http://" + const.host + ':' + const.port + '/get_reply/'
        requests.post(url=url_client, headers=params)
        print("Reply phase ended:", time.time())
        if self.to_host is not None and self.to_port is not None:
            url = "http://" + self.to_host + ':' + self.to_port + '/commit_ack/'
            requests.post(url=url, headers=params)
        else:

            new_msg = [const.open_brac, params[const.VIEW], params[const.MSG_SEQ],
                       params[const.TYPE], params[const.MSG], const.close_brac]
            new_params = {
                      const.MSG: ", ".join(new_msg)
                      }
            print("Ended commit_ack:", time.time())
            print("total time ended", time.time())
            #url_draw = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
            #requests.post(url=url_draw, headers=new_params)
            return

    def commit_ack(self, request):
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

            msg = [
                    const.open_brac, request.headers[const.VIEW], request.headers[const.MSG_SEQ],
                    request.headers[const.TYPE],
                    request.headers[const.MSG],
                    const.close_brac
                 ]

            params = {const.VIEW: self.view_num,
                      const.MSG_SEQ: str(int(request.headers[const.MSG_SEQ]) + 1),
                      const.TYPE: const.COMMITACK,
                      const.MSG: ", ".join(msg),
                      }
        print("Node "+self.view_num+": ", params)
        #url_draw = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
        #requests.post(url=url_draw, headers=params)
        self.next_commit_ack(params)
        return web.Response(text="My message")

    def create_commit_msg(self, request):
        if self.view_num == "3":
            print("Commit Phase Started:", time.time())
        msg = [
                const.open_brac, request[const.VIEW], request[const.MSG_SEQ],
                request[const.TYPE],
                request[const.MSG],
                const.close_brac
               ]
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
        start_time = time.time()
        if self.view_num == "1":
            print("Prepare Phase started:", start_time)
            msg = [
                    const.open_brac, request.headers[const.VIEW], request.headers[const.MSG_SEQ],
                    request.headers[const.TYPE], request.headers[const.DATA], const.close_brac
                  ]
            print(msg)
            # print("Commit", request.headers[const.commit])
            params = {const.VIEW: self.view_num,
                      const.MSG_SEQ: str(int(request.headers[const.MSG_SEQ]) + 1),
                      const.TYPE: const.PRE_PREPARE,
                      const.MSG: ", ".join(msg),
                      const.prep: str(int(request.headers[const.prep]) + 1),
                      const.commit: str(int(request.headers[const.commit])),
                      }
        else:

            msg = [
                   const.open_brac, request.headers[const.VIEW], request.headers[const.MSG_SEQ],
                   request.headers[const.TYPE], request.headers[const.MSG], const.close_brac
                  ]
            params = {const.VIEW: self.view_num,
                  const.MSG_SEQ: str(int(request.headers[const.MSG_SEQ]) + 1),
                  const.TYPE: const.PREPARE,
                  const.MSG: ", ".join(msg),
                  const.prep: str(int(request.headers[const.prep]) + 1),
                  const.commit: str(int(request.headers[const.commit])),
                  }

        # url_diagram = "http://" + const.host_diagram + ':' + const.port_diagram + '/change_text/'
        # result = requests.post(url=url_diagram, headers=params)

        # const.prep = const.prep + 1
        # print("Prep msg", params[const.prep])
        if self.to_port and self.to_host and int(params[const.prep]) < 2 * const.faulty:
            # print("Node: "+self.view_num+": ", params)
            url = "http://" + self.to_host + ':' + self.to_port + '/prep/'
            response = requests.post(url=url, headers=params)

            if self.view_num == "1":
                print("Prepare Phase Ended:", time.time())

            response_content = self.create_commit_msg(json.loads(response.text))
            if self.view_num == "1":
                print("Commit Phase ended at: ", time.time())
                response_content = self.commit_ack(response_content)
                print("Node: " + self.view_num + ": ", response_content)
                return web.Response(text="My message")
            else:
                response_content = json.dumps(response_content)

                print("Node: "+self.view_num+": ", response_content)
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
        app = web.Application()
        here = Path(__file__).resolve().parent
        aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(here)))

        app.router.add_route('GET', '/initiate/', self.initiating)
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

    @aiohttp_jinja2.template('display.html')
    def initiating(self,request):
        print("in intiating")
        return {'stage': 'initiating'}

# https://stackoverflow.com/questions/12977517/python-equivalent-of-d3-js
