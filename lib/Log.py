#coding:utf-8
import logging  
  
# 配置日志信息  
class Log(object):
    def __init__(self, file_name="myapp.log"):
        logging.basicConfig(level=logging.DEBUG,  
                            format='%(asctime)s %(name)-12s %(threadName)s  %(funcName)s %(levelname)-8s -%(lineno)d %(message)s',  
                            datefmt='%m-%d %H:%M',  
                            filename=file_name,  
                            filemode='w')  
        # 定义一个Handler打印INFO及以上级别的日志到sys.stderr  
        console = logging.StreamHandler()  
        console.setLevel(logging.INFO)  
        # 设置日志打印格式  
        formatter = logging.Formatter('%(asctime)-12s: %(threadName)s  %(funcName)s %(levelname)-8s -%(lineno)d - %(message)s')  
        console.setFormatter(formatter)  
        # 将定义好的console日志handler添加到root logger  
        logging.getLogger('').addHandler(console)  