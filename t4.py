#/usr/bin/python
#_*_coding:utf-8_*_
'''
Created on 2016??12??13??

@author: workstation
'''
import chardet

a= u'บร'
print chardet.detect(a.encode('gbk'))
print a.encode('gbk')
