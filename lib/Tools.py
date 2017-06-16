#coding:utf-8
import datetime
class Tools(object):
    
    
    def __init__(self):
        pass

    @staticmethod
    def get_today_str():
        td =  datetime.date.today()
        #return td.strftime("%Y%m%d")
        return "20161214"

if __name__ == "__main__":
    print Tools.get_today_str()