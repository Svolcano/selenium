#coding:utf-8

import pymysql
from lib.Tools import Tools

class DB(object):
    _db_host = '123.56.72.57'
    _db_user = 'check_user'
    _db_pwd = '654321123456'
    _db_def = 'test_check'
    _db_port = 3306
    #===========================================================================
    # _db_host = 'localhost'
    # _db_user = 'root'
    # _db_pwd = '.'
    # _db_def = 'test_db'
    # _db_port = 3306
    #===========================================================================
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=DB._db_host,
                                        user=DB._db_user, 
                                        passwd=DB._db_pwd,
                                        db=DB._db_def,
                                        port=DB._db_port,
                                        )
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print e
            self.conn = None
            self.cursor = None
    
    def query(self, sql):
        try:
            self.cursor.execute(sql)
            all_ret = self.cursor.fetchall()
            return all_ret;
        except Exception as e:
            return None
        
    def excutemany(self, sql, arg):
        try:
            n = self.cursor.executemany(sql, arg)
            self.conn.commit()
            return True
        except Exception as e:
            print e
            return False
        
    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
        except:
            pass
        try:
            if self.conn:
                self.conn.close()
        except:
            pass

if __name__ == "__main__":
    sql = 'INSERT INTO test(id,NAME) VALUES(%s,%s)'
    v =[(2,'1'),[3,'1']]
    db = DB()
    print db.excutemany(sql, v)
    db.close()   
        