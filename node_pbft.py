#! /opt/anaconda3/bin/python3



import asyncio
from random import random

import aiohttp
from aiohttp import web
import constant

class PBFTHandler:
    REQUEST = 'request'

    async def _post(self, nodes, command, json_data):
        '''
        Broadcast json_data to all node in nodes with given command.
        input:
            nodes: list of nodes
            command: action
            json_data: Data in json format.
        '''
        if not self._session:
            timeout = aiohttp.ClientTimeout(self._network_timeout)
            self._session = aiohttp.ClientSession(timeout=timeout)
        for i, node in enumerate(nodes):
            if random() > self._loss_rate:
                self._log.debug("make request to %d, %s", i, command)
                try:
                    _ = await self._session.post(self.make_url(node, command), json=json_data)
                except Exception as e:
                    #resp_list.append((i, e))
                    self._log.error(e)
                    pass
    async def synchronize(self):
        '''
        Broadcast current checkpoint and all the commit certificate
        between next slot of the checkpoint and commit upperbound.

        output:
            json_data = {
                'checkpoint': json_data = {
                    'next_slot': self._next_slot
                    'ckpt': json.dumps(ckpt)
                }
                'commit_certificates':commit_certificates
                    (Elements are commit_certificate.to_dict())
            }
        '''
        # TODO: Only send bubble slot message instead of all.
        self._sync_interval = 3
        #self._ckpt.get_commit_upperbound()
        json_data = {
            'checkpoint': 1,
            'commit_certificates':2
        }
        #await self._post(self._nodes, PBFTHandler.RECEIVE_SYNC, json_data)


    async def get_request(self, request):
        '''
        Handle the request from client if leader, otherwise
        redirect to the leader.
        '''
        # self._log.info("---> %d: on request", self._index)

        # if not self._is_leader:
        #     if self._leader != None:
        #         raise web.HTTPTemporaryRedirect(self.make_url(
        #             self._nodes[self._leader], PBFTHandler.REQUEST))
        #     else:
        #         raise web.HTTPServiceUnavailable()
        # else:
        #     json_data = await request.json()
        #     await self.preprepare(json_data)
        #     return web.Response()
        print("get_request", request)
        text = "inside node get requst"
        return web.Response(text=text)


if __name__ == "__main__":
    pbft = PBFTHandler()


    asyncio.ensure_future(pbft.synchronize())
    #asyncio.ensure_future(pbft.garbage_collection())

    app = web.Application()
    print("mlkdfmfdflkvmdvlkm")
    app.add_routes([web.post('/' + PBFTHandler.REQUEST, pbft.get_request)])
    web.run_app(app, host=constant.host, port=constant.port, access_log=None)
