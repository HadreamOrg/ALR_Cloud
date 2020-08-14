# coding=utf-8
# author: Lan_zhijiang
# description: websocket服务器

import websockets
import asyncio
import json
from network_communicator.handler.websocket_handler import AlrCloudWebsocketHandler


class AlrCloudWebsocketServer():

    def __init__(self, class_log):

        self.cloud_setting = json.load(open("./setting/cloud_setting/basic_setting.json", "r", encoding="utf-8"))
        self.websocket = websockets.serve(self.main_logical, self.cloud_setting["ip"], self.cloud_setting["websocketPort"])
        self.acwh = AlrCloudWebsocketHandler(class_log)
        self.log = class_log

    async def confirm_permission(self, websocket):

        """
        确认身份
        :param websocket:
        :return:
        """
        self.log.add_log(1, "WebsocketServer: Start confirming permission")

        is_pass = False
        account_password_list = json.load(open("./data_folder/file/websocket_account_password_list.json", "r", encoding="utf-8"))
        account = await websocket.recv()
        password = await websocket.recv()
        for waitConfirm in account_password_list:
            if waitConfirm["account"] == account and waitConfirm["password"] == password:
                self.log.add_log(1, "WebsocketServer: Confirm permission success")
                websocket.send("0")
                is_pass = True
        if not is_pass:
            self.log.add_log(2, "WebsocketServer: Confirm permission failed: AP is not paired")
            websocket.send("1")
            websocket.close()

    async def main_logical(self, websocket, path):

        """
        websocket服务器主逻辑
        :return:
        """
        await self.confirm_permission(websocket)
        await self.acwh.handle(websocket)

