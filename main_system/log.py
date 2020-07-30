# coding=utf-8
# author: Lan_zhijiang
# description: The file record and output logs

import time
import datetime
import os


class AlrCloudLog():

    def __init__(self):  

        self.logLevelList = [
           "DEBUG", "INFO", "WARNING", "ERROR", "FATAL"
        ]

    def get_log_file_path(self):

        """
        获取log文件路径
        :return:
        """
        basic_path = "./data_folder/log/cloud/"
        log_file_name = self.get_date() + ".txt"
        if os.path.exists(basic_path + log_file_name) is False:
            create_log_file = open(basic_path + log_file_name, "w")
            create_log_file.close()
        else:
            pass
        return basic_path + log_file_name

    def get_time_stamp(self):

        """
        获取当前时间戳，整数化字符化
        :return:
        """
        return str(int(time.time()))

    def get_date(self):

        """
        获取当前日期
        :return:
        """
        return str(datetime.date.today())

    def add_log(self, level, content, is_print=True):

        """
        添加log
        :param level: log级别
        :param content: log内容
        :param is_print: 是否打印
        :return:
        """
        log = "[" + level + "] " + self.get_time_stamp() + " " + content
        if is_print:
            print(log)
        try:
            log_file = open(self.get_log_file_path(), "w")
            log_file.write('\r\n' + log)
            log_file.close()
        except IOError:
            return 1
        else:
            return 0