import logging
import pytest


class MyLogger:
    def __init__(self):
        """format常用格式说明
        %(levelno)s: 打印日志级别的数值
        %(levelname)s: 打印日志级别名称
        %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s: 打印当前执行程序名
        %(funcName)s: 打印日志的当前函数
        %(lineno)d: 打印日志的当前行号
        %(asctime)s: 打印日志的时间
        %(thread)d: 打印线程ID
        %(threadName)s: 打印线程名称
        %(process)d: 打印进程ID
        %(message)s: 打印日志信息"""
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        # self.handler = logging.FileHandler("log.txt")
        # self.handler.setLevel(logging.ERROR)
        # self.handler.setFormatter(self.formatter)
        # self.logger.addHandler(self.handler)

        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.console)

    def log(self):
        return self.logger


log = MyLogger().log()

if __name__ == '__main__':
    log = MyLogger().log()
    log.info('abc')
