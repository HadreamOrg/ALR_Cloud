# coding=utf-8
# author: Lan_zhijiang
# description: 存储http/websocket请求的对应处理函数的类

from network_communicator.connection_manager.websocket_server_manager import AlrCloudWebsocketServerManager


class AlrCloudHttpHandleFunction():

    def __init__(self, class_log):

        self.httpHandleFunctionList = {
            "getWebsocketPermission": AlrCloudWebsocketServerManager(class_log).sign_up_permission
        }


class AlrCloudWebsocketHandleFunction():

    def __init__(self, class_log):

        self.websocketHandleFunctionList = {
        }
