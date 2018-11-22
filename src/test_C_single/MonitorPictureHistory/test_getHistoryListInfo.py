#coding=utf-8
'''
Created on 2018年8月8日

@author: chenyongfa
'''
import unittest
from common.common import rq_getHistoryListInfo
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

class Test_getHistoryListInfo(ParametrizedTestCase):
    u'''currentPage: 1
        endTime: 
        orderType: desc
        pageSize: 10
        sid: 4329
        startTime: 
    '''
    def test_a(self):
        u''' 不传参 '''
        response = rq_getHistoryListInfo(self.param)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100001, "this case is failed")
        
    def test_b(self):
        u''' 传正确的sid '''
        response = rq_getHistoryListInfo(self.param,sid=getConf("data","sid"))
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000 and len(response["data"])!=0, "this case is failed")
        
    def test_c(self):
        u''' 传错误的sid '''
        response = rq_getHistoryListInfo(self.param,sid="000000000")
        print response
        u''' check'''
        self.assertTrue(response["status"]==100001, "this case is failed")
        
    def test_d(self):
        u''' 正确的sid 错误的endtime '''
        response = rq_getHistoryListInfo(self.param,sid=getConf("data","sid"),endTime="8:00")
        print response
        u''' check'''
        self.assertTrue(response["status"]==100001, "this case is failed")
        
    def runTest(self):
        pass

if __name__ == "__main__":
    
    a = Test_getHistoryListInfo()
    a.test_d()
    