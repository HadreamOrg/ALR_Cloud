# coding=utf-8
# author: Lan_zhijiang
# description: 存储http/websocket请求的对应处理函数的类

from network_communicator.connection_manager.websocket_server_manager import AlrCloudWebsocketServerManager


class AlrCloudHttpHandleFunction():

    def __init__(self):

        self.httpHandleFunctionList = {
            "getWebsocketPermission": AlrCloudWebsocketServerManager().sign_up_permission
        }
