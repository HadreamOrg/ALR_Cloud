# coding=utf-8
# author: Lan_zhijiang
# description: 处理来自HTTP的请求的分类器


class AlrCloudHttpHandler():

    def __init__(self):

        self.request_data = None
        self.api_list = open("./data_folder/file/api_list.json", "r", encoding="utf-8").read()

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

