# coding=utf-8
# author: Lan_zhijiang
# description: 处理来自HTTP的请求的分类器

import json
from network_communicator.handler.handle_function import AlrCloudHttpHandleFunction


class AlrCloudHttpHandler():

    def __init__(self, class_log):

        self.request_data = None
        self.api_list = json.load(open("./data_folder/file/http_api_list.json", "r", encoding="utf-8"))
        self.standard_response = json.load(open("./data_folder/file/standard_response.json", "r", encoding="utf-8"))
        self.handle_function = AlrCloudHttpHandleFunction(class_log)
        self.log = class_log

    def set_request_data(self, request_data):

        """
        设置由请求端发送而来的数据到类全局中
        :param request_data: 请求数据
        :return:
        """
        self.request_data = request_data

    def handle_request(self):

        """
        开始处理请求
        :return:
        """
        response = self.standard_response

        for nowProcessingCommand in self.request_data["event"]["request"]:
            processed_command_count = 0
            for waitConfirmCommand in self.api_list:
                if waitConfirmCommand["commandName"] == nowProcessingCommand["commandName"]:
                    self.log.add_log(1, "HttpHandler: Start processing command: " + nowProcessingCommand["commandName"])

                    processed_command_count += 1
                    break
            if processed_command_count == 0:
                self.log.add_log(2, "HttpHandler: There is no command compare with! CommandName: " + nowProcessingCommand["commandName"])
                response["event"]["response"][nowProcessingCommand["commandName"]] = {
                    "status": 1,
                    "errMsg": "No compared command in the api list"
                }
            else:
                response = self.handle_function.httpHandleFunctionList[nowProcessingCommand["commandName"]](nowProcessingCommand["param"], response)

        response["head"]["timeStamp"] = self.log.get_time_stamp()
