# coding=utf-8
# author: Lan_zhijiang
# description: websocket服务器管理器

import json


class AlrCloudWebsocketServerManager():

    def __init__(self, class_log):

        self.log = class_log

    def sign_up_permission(self, param):

        """
        注册websocket请求权限
        :param param
        :return:
        """
        account = param["account"]
        password = param["password"]
        self.log.add_log(1, "WebsocketServerManager: Sign up permission for: " + account)
        account_password_list = json.load(open("./data_folder/file/websocket_account_password_list.json", "r", encoding="utf-8"))
        account_password_list.append({"account": account, "password": password})
