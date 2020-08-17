# coding=utf-8
# author: Lan_zhijiang
# description: 用Flask创建一个HTTP服务器

from flask import Flask
from flask import request
from network_communicator.handler.http_handler import AlrCloudHttpHandler
import json

cloud_setting = json.load(open("./setting/cloud_setting/basic_setting.json", encoding="utf-8"))
flask_app = Flask(__name__)
achhc = 0


def run_flask(class_log):

    """
    启动Flask服务器
    :return:
    """
    class_log.add_log(1, "HttpServer: Start http server...")

    flask_app.run(host=cloud_setting["hostIp"], port=cloud_setting["httpPort"])
    global achhc
    achhc = AlrCloudHttpHandler(class_log)


@flask_app.route('/api', methods=['POST'])
def route_api():

    """
    处理请求到/api路径下的请求
    :return:
    """
    achhc.set_request_data(request.get_json(force=True))
    return json.dumps(achhc.handle_request())


