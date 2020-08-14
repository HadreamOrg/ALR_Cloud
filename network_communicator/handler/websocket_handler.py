# coding=utf-8
# author: Lan_zhijiang
# description: 处理websocket业务逻辑的类

import asyncio
import websockets
import json
from network_communicator.handler.handle_function import AlrCloudWebsocketHandleFunction


class AlrCloudWebsocketHandler():

    def __init__(self, class_log):

        self.log = class_log
        self.api_list = json.load(open("./data_folder/file/websocket_api_list.json", "r", encoding="utf-8"))
        self.handle_function = AlrCloudWebsocketHandleFunction(class_log)

    async def handle(self, websocket):

        """
        分配函数
        :param websocket:
        :return:
        """
        while True:
            processed_command_count = 0
            command_name = await websocket.recv()
            for waitConfirmCommand in self.api_list:
                if waitConfirmCommand["commandName"] == command_name:
                    self.log.add_log(1, "WebsocketHandler: Start processing command: " + command_name)
                    processed_command_count += 1
                    command_info = waitConfirmCommand
                    break

            if processed_command_count == 0:
                self.log.add_log(2, "WebsocketHandler: There is no command compare with! CommandName: " + command_name)
                websocket.send("error")
            else:
                if command_info["Param"] is not None:
                    websocket.send("param")
                    param = await websocket.recv()
                    await self.handle_function.websocketHandleFunctionList[command_info["commandName"]](param, websocket)
                    websocket.send("next")
                    self.log.add_log(1, "WebsocketHandler: Command: " + command_name + "processed")

