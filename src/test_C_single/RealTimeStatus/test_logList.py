#coding=utf-8
import unittest
from common.common import rq_logList
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

class Test_logList(ParametrizedTestCase):
    u''' params currentPage:1  endtime:""  orderName:"addtime"  orderType:"desc"  pageSize:"10"  sid:"4354"  starttime:"" '''
    def test_a(self):
        u''' correct params '''
        response = rq_logList(self.param,currentPage=1,endtime="",orderName="addtime",orderType="desc",pageSize="10",sid=getConf('data', 'sid'),starttime="")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000 and len(response['data']['list'])>0, 'this case is failed')
        
    def test_b(self):
        u''' wrong orderName '''
        response = rq_logList(self.param,currentPage=1,endtime="",orderName="abc",orderType="desc",pageSize="10",sid=getConf('data', 'sid'),starttime="")
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_c(self):
        u''' wrong time '''
        response = rq_logList(self.param,currentPage=1,endtime="2018-08-32",orderName="addtime",orderType="desc",pageSize="10",sid=getConf('data', 'sid'),starttime="2018-08-32")
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_d(self):
        u''' no   sid '''
        response = rq_logList(self.param,currentPage=1,endtime="",orderName="addtime",orderType="desc",pageSize="10",starttime="")
        print response
        u''' check '''
        self.assertTrue(response['status']==100001, 'this case is failed')
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_logList()
    a.test_a()
    a.test_b()
    a.test_c()
    a.test_d()
