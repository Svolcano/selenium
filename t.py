#/usr/bin/python
#_*_coding:utf-8_*_
'''
Created on 2016??12??13??

@author: workstation
'''

  
logging.info('Jackdaws love my big sphinx of quartz.')  
  
logger1 = logging.getLogger('myapp.area1')  
logger2 = logging.getLogger('myapp.area2')  
  
logger1.debug('Quick zephyrs blow, vexing daft Jim.')  
logger1.info('How quickly daft jumping zebras vex.')  
logger2.warning('Jail zesty vixen who grabbed pay from quack.')  
logger2.error('The five boxing wizards jump quickly.') 