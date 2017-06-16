#coding:utf-8

class SQLMgr(object):
    
    
    def __init__(self):
        pass
    
    @staticmethod
    def insert_many():
        sql = '''
        INSERT INTO stock_plate(plate_code, plate_name,stock_cnt,price_avg,wave_cnt,wave_range,vol,amount,first_stock_code,
        first_stock_name, first_stock_price,first_stock_wave_range,remark,TIME)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        return sql
    