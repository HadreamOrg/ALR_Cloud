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

    def handle(self, websocket):

        """
        主处理函数
        :param websocket: 传递过来的websocket连接
        :return:
        """
        self.log.add_log(1, "WebsocketHandler: Waiting for command...")

        while True:
            processed_command_count = 0
            command_info = websocket.ws_recv()
            for waitConfirmCommandInfo in self.api_list:
                if waitConfirmCommandInfo["commandName"] == command_info["commandName"]:
                    self.log.add_log(1, "WebsocketHandler: Start processing command: " + command_info["commandName"])
                    processed_command_count += 1
                    confirm_command_info = waitConfirmCommandInfo
                    break

            if processed_command_count == 0:
                self.log.add_log(2, "WebsocketHandler: There is no command compared with! CommandName: " + command_info["commandName"])
                websocket.ws_send({"command": "not_found"})
                websocket.shutdown()
            else:
                if confirm_command_info["param"] is not None:
                    self.log.add_log(1, "WebsocketHandler: Ask for the param...")
                    param = command_info["param"]
                else:
                    param = {}
                status = self.handle_function.websocketHandleFunctionList[command_info["commandName"]](param, websocket)
                if status == 0:
                    websocket.ws_send({"command": "next"})
                    self.log.add_log(1, "WebsocketHandler: Command: " + command_info["commandName"] + "was processed")
                else:
                    return "error_done"
