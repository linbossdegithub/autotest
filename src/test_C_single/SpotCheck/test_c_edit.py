#coding=utf-8
import unittest

from common.common import rq_edit
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_edit (ParametrizedTestCase):
    u''' params id: 318, name: "123333", cycle: 2, month: 1, week: 0, time: "09:00", rate: 5, isSendSpockEmail: 0'''
        
    def test_a(self):
        u''' wrong month '''
        response = rq_edit (self.param,id=getConf('data','tem_id'),name=getConf('data', 'tem_spot_name'),cycle=2,month=32, week=0, time="09:00", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u''' wrong time '''
        response = rq_edit (self.param,id=getConf('data','tem_id'),name=getConf('data', 'tem_spot_name'),cycle=2,month=1, week=0, time="9", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_c(self):
        u''' wrong tem_id '''
        response = rq_edit (self.param,id="0000",name=getConf('data', 'tem_spot_name'),cycle=2,month=1, week=0, time="abc", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_d(self):
        u''' no cycle '''
        response = rq_edit (self.param,id=getConf('data','tem_id'),name=getConf('data', 'tem_spot_name'),month=1, week=0, time="abc", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_e(self):
        u''' correct params '''
        response = rq_edit (self.param,id=getConf('data','tem_id'),name=getConf('data', 'tem_spot_name'),cycle=2,month=1, week=0, time="09:00", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_edit ()
    a.test_a()
#     a.test_b()
#     a.test_c()
#     a.test_d()
#     a.test_e()
         
    

