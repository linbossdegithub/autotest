#coding=utf-8
import unittest
from common.common import rq_getScreenList
from parametrizedTestCase import ParametrizedTestCase


class Test_getScreenList(ParametrizedTestCase):
    u''' FilterList:"",Keywords:"",OrderName:"screenName",OrderType:"desc",PageIndex:"1",PageSize:"10",Status:0,sids:[]'''
    def test_a(self):
        u''' correct params '''
        response = rq_getScreenList(self.param,FilterList="",Keywords="",OrderName="screenName",OrderType="desc",PageIndex="1",PageSize="10",Status=0,sids=[])
        print response
        u'check'
        self.assertTrue(response['status']==100000 and response['data']>0, 'this case is failed')
    def test_b(self):
        u''' wrong OrderName '''
        response = rq_getScreenList(self.param,FilterList="",Keywords="",OrderName="abc",OrderType="desc",PageIndex="1",PageSize="10",Status=0,sids=[])
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
    def test_c(self):
        u''' wrong OrderName '''
        response = rq_getScreenList(self.param,FilterList="",Keywords="",OrderName="screenName",OrderType="desc",PageIndex="1",PageSize="10",Status=0,sids=['000'])
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
        
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_getScreenList()
    a.test_a()
    a.test_b()
    a.test_c()
        
    
