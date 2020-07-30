# coding=utf-8
# author: Lan_zhijiang
# description: websocket服务器

import websockets
import asyncio
import json


class AlrCloudWebsocketServer():

    def __init__(self):

        self.cloud_setting = json.load(open("./setting/cloud_setting/basic_setting.json", "r", encoding="utf-8"))
        self.websocket = websockets.serve(self.main_logical, self.cloud_setting["ip"], self.cloud_setting["websocketPort"])

    async def confirm_permission(self, websocket):

        """
        确认身份
        :param websocket:
        :return:
        """
        is_pass = False
        account_password_list = json.load(open("./data_folder/file/websocket_account_password_list.json", "r", encoding="utf-8"))
        account = await websocket.recv()
        password = await websocket.recv()
        for waitConfirm in account_password_list:
            if waitConfirm["account"] == account and waitConfirm["password"] == password:
                websocket.send("0")
                is_pass = True
        if not is_pass:
            websocket.send("1")

    async def main_logical(self, websocket, path):

        """
        websocket服务器主逻辑
        :return:
        """
        await self.confirm_permission(websocket)
