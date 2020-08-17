# coding=utf-8
# author: Lan_zhijiang
# description: websocket服务器

import json
from pywss import Pyws, route
from network_communicator.handler.websocket_handler import AlrCloudWebsocketHandler

class_log_global = 0


class AlrCloudWebsocketServer():

    def __init__(self, class_log):

        self.cloud_setting = json.load(open("./setting/cloud_setting/basic_setting.json", "r", encoding="utf-8"))
        self.acwh = AlrCloudWebsocketHandler(class_log)
        self.log = class_log

        global class_log_global
        class_log_global = class_log

    def run_websocket_server(self):

        """
        启动websocket服务器
        :return:
        """
        self.log.add_log(1, "WebsocketServer: Start websocket server... ")
        self.log.add_log(1, "WebsocketServer: WsAddr: ws://" + self.cloud_setting["hostIp"] + ":" + str(self.cloud_setting["websocketPort"]))

        ws = Pyws(__name__, address=self.cloud_setting["hostIp"], port=self.cloud_setting["websocketPort"])
        ws.serve_forever()

    def confirm_permission(self, websocket):

        """
        确认身份
        :param websocket:
        :return:
        """
        self.log.add_log(1, "WebsocketServer: Confirming permission...")

        is_pass = False
        account_password_list = json.load(open("./data_folder/file/websocket_account_password_list.json", "r", encoding="utf-8"))
        websocket.ws_send({"command": "ap"})
        ap = websocket.ws_recv()
        account, password = ap["account"], ap["password"]
        for waitConfirm in account_password_list:
            if waitConfirm["account"] == account and waitConfirm["password"] == password:
                self.log.add_log(1, "WebsocketServer: Permission confirmed")
                websocket.ws_send({"command": "pass"})
                is_pass = True
        if not is_pass:
            self.log.add_log(2, "WebsocketServer: Permission denied: A/P was not paired")
            websocket.ws_send({"command": "fail"})
            websocket.shutdown()

    def main_logical(self, websocket, data):

        """
        websocket服务器主逻辑
        :param websocket: 连接对象
        :param data: 接收的数据
        :return:
        """
        self.log.add_log(1, "WebsocketServer: Receive a new connection. Data: " + str(data))
        self.confirm_permission(websocket)
        return self.acwh.handle(websocket)


@route('/api')
def route_api(websoscket, data):               # 这后面的还没测试过

    """
    处理连接到ws/api下的连接给主逻辑
    :param websoscket: 连接对象
    :param data: 接收的数据
    :return:
    """
    acws = AlrCloudWebsocketServer(class_log_global)
    return acws.main_logical(websoscket, data)

