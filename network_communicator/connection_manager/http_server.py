# coding=utf-8
# author: Lan_zhijiang
# description: 用Flask创建一个HTTP服务器

from flask import Flask
from flask import request
from network_communicator.handler.http_handler import AlrCloudHttpHandler
import json

port = [5000]
flask_app = Flask(__name__)


def run_flask(class_log):

    """
    启动Flask服务器
    :return:
    """
    flask_app.run()
    achhc = AlrCloudHttpHandler(class_log)
    global achhc


@flask_app.route('/api', methods=['POST'])
def route_api(self):

    """
    处理请求到/api路径下的请求
    :return:
    """
    achhc.set_request_data(request.get_json(force=True))
    return json.dumps(achhc.handle_request())


