import asyncio
from aiohttp import web
from aiohttp import ClientSession
import requests
import time
"""
['ATTRS', 'POST_METHODS', '_MutableMapping__marker', '__abstractmethods__', '__bool__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__orig_bases__', '__parameters__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_cache', '_client_max_size', '_content_dict', '_content_type', '_headers', '_http_date', '_loop', '_match_info', '_message', '_method', '_parse_content_type', '_payload', '_payload_writer', '_post', '_prepare_hook', '_protocol', '_read_bytes', '_rel_url', '_state', '_stored_content_type', '_task', '_transport_peername', '_transport_sslcontext', '_version', 'app', 'body_exists', 'can_read_body', 'charset', 'clear', 'clone', 'config_dict', 'content', 'content_length', 'content_type', 'cookies', 'forwarded', 'get', 'has_body', 'headers', 'host', 'http_range', 'if_modified_since', 'if_range', 'if_unmodified_since', 'items', 'json', 'keep_alive', 'keys', 'loop', 'match_info', 'message', 'method', 'multipart', 'path', 'path_qs', 'pop', 'popitem', 'post', 'protocol', 'query', 'query_string', 'raw_headers', 'raw_path', 'read', 'rel_url', 'release', 'remote', 'scheme', 'secure', 'setdefault', 'task', 'text', 'transport', 'update', 'url', 'values', 'version', 'writer']
"""


import asyncio
from aiohttp import web
import json
import constant as const


async def initiate_pbft(url):
    print("Url is", url)
    global char_size
    params = {
                const.VIEW: "0",
                const.MSG_SEQ: "0",
                const.TYPE: const.REQUEST,
                const.prep: "-1",
                const.commit: "0",

             }

    jsons = {const.DATA: const.get_string(char_size)}

    #print("data_string =", params)
    print("total time started", time.time())
    response = requests.post(url=url, params=params, headers=params, data=json.dumps(jsons))
    print(response.__attrs__)
    print(response._content)

char_size = input()

app = web.Application(client_max_size=40000 * 2 ** 10)
loop = asyncio.get_event_loop()
handler = app.make_handler()


try:
    loop.run_until_complete(initiate_pbft("http://" + const.host_1 + ':' + const.port_1 + '/prep/'))
except KeyboardInterrupt:
    pass
finally:
    loop.close()
loop.close()

"""
host = 'localhost'
port = '8028'
app = web.Application()
app.router.add_route('GET', '/node1/', hello)
web.run_app(app, host=host, port=port, access_log=None)
"""
#  ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-54-226-110-230.compute-1.amazonaws.com
#  ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-54-164-88-108.compute-1.amazonaws.com
#  ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-184-72-127-166.compute-1.amazonaws.com
#  ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-54-242-182-233.compute-1.amazonaws.com
#  ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-3-95-31-142.compute-1.amazonaws.com

# ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-18-205-244-82.compute-1.amazonaws.com


# ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-54-227-2-149.compute-1.amazonaws.com
# ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-54-226-195-115.compute-1.amazonaws.com
# ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-18-234-141-77.compute-1.amazonaws.com
# ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-184-72-207-159.compute-1.amazonaws.com
# ssh -i /Users/sonalisuri/Desktop/spft-instance.pem ubuntu@ec2-18-205-244-82.compute-1.amazonaws.com

