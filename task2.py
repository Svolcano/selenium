#coding:utf-8

import time
import datetime
import threading
import Queue
import logging

from lib.DB import DB
from lib.SQLMgr import SQLMgr
from lib.Tools import Tools
from lib.Log import Log

logger = logging.getLogger()

task_queue = Queue.Queue()
result_queue = Queue.Queue()

def filter(high, low):
    logger.info("")
    return float((high-low))/float(low) > 0.1

def worker(task_queue, result_queue):
    logger.info("")
    while 1:
        try:
            data = task_queue.get(timeout=20) #20 no data , seems over
            ret = filter(data['high'], data['low'])
            logger.info("%s %s %s" % ( ret, data['high'], data['low']))
            if ret:
                ret_data = [
                    data['code'],
                    data['tr_date'],
                    data['date_type'],
                    data['ex_type'],
                    'zdjl',
                    'test',
                    datetime.datetime.now(),
                    ]
                result_queue.put(ret_data)
        except Exception as e:
            logger.info("worker break %s", e)
            break
    #task_queue.task_done()
        
def db_writer(result_queue, db):
    logger.info("")
    count = 0
    write_list = []
    while 1:
        try:
            data = result_queue.get(20) #60s no data come , seem write done
            if count == 10:
                count = 0
                logger.info("insert result: %s", db.excutemany(SQLMgr.insert_stock_xg_many(), write_list))
                write_list = []
            count += 1
            write_list.append(data)
        except Exception as e:
            logger.info("db break %s", e)
            break
    #result_queue.task_done()

if __name__ == "__main__":
    Log("test.log")
    try:
        db = DB()
        all_data = db.query(SQLMgr.get_all_kline_info(Tools.get_today_str()))
        if all_data:
            for row in all_data:
                task_queue.put(row)
        print all_data
        worker_thread_num = 4
        worker_thread_list = []
        for i in range(worker_thread_num):
            t = threading.Thread(target=worker, args=(task_queue, result_queue))
            worker_thread_list.append(t)
            
        database_thread = threading.Thread(target=db_writer, args=(result_queue, db))
        database_thread.setDaemon(True)
        database_thread.start()
        #
        for t in worker_thread_list:
            t.start()
            
        for t in worker_thread_list:
            t.join()
        database_thread.join()    
        logger.info("done")
    except Exception as e:
        print e
    finally:
        db.close()




