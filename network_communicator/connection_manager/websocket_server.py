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
        self.websocket_serve = websockets.serve(self.main_logical, self.cloud_setting["hostIp"], self.cloud_setting["websocketPort"])
        self.acwh = AlrCloudWebsocketHandler(class_log)
        self.log = class_log

    def run_websocket_server(self):

        """
        启动websocket服务器
        :return:
        """
        if __name__ == "__main__":
            self.log.add_log(1, "WebsocketServer: Start websocket server... ")
            self.log.add_log(1, "WebsocketServer: WsIp: " + self.cloud_setting["hostIp"] + ":" + self.cloud_setting["websocketPort"])

            asyncio.get_event_loop().run_until_complete(self.websocket_serve)
            asyncio.get_event_loop().run_forever()

    async def confirm_permission(self, websocket):

        """
        确认身份
        :param websocket:
        :return:
        """
        self.log.add_log(1, "WebsocketServer: Confirming permission...")

        is_pass = False
        account_password_list = json.load(open("./data_folder/file/websocket_account_password_list.json", "r", encoding="utf-8"))
        account = await websocket.recv()
        password = await websocket.recv()
        for waitConfirm in account_password_list:
            if waitConfirm["account"] == account and waitConfirm["password"] == password:
                self.log.add_log(1, "WebsocketServer: Permission confirmed")
                websocket.send("0")
                is_pass = True
        if not is_pass:
            self.log.add_log(2, "WebsocketServer: Permission denied: A/P was not paired")
            websocket.send("1")
            websocket.close()

    async def main_logical(self, websocket, path):

        """
        websocket服务器主逻辑
        :return:
        """
        await self.confirm_permission(websocket)
        await self.acwh.handle(websocket)

