#coding:utf-8
from lib.DB import DB

class SQLMgr(object):
    
    
    def __init__(self):
        pass
    
    @staticmethod
    def insert_many():
        sql = '''
        INSERT INTO stock_plate(plate_code,first_stock_code, plate_name,stock_cnt,price_avg,wave_cnt,wave_range,vol,amount,
        first_stock_name, first_stock_price, first_stock_wave_cnt, first_stock_wave_range,remark,TIME)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        return sql
    
    @staticmethod
    def get_all_kline_info(now):
        sql = '''
            select * 
            from stock_kline
            where tr_date='%s' and date_type=0 and ex_type=1
        ''' % now
        return sql
    
    @staticmethod
    def insert_stock_xg_many():
        sql = '''
            insert into stock_xg(code, tr_date, date_type, ex_type, xg, remark, time)
            values(%s, %s, %s, %s, %s, %s, %s)
        '''
        return sql
    
if __name__ == "__main__":
    db = DB()
    print db.excutemany(SQLMgr.insert_stock_xg_many(),[('11',1,1,1,'123','111','2016-11-11'),])
    db.close()