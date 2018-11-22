#coding=utf-8
import unittest
from common.common import rq_set
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_set(ParametrizedTestCase):
    u''' params id: 4354, tempId: 320, cycle: 0, month: 1, week: 0, time: "09:00", rate: 5, isSendSpockEmail: 0'''
    def test_a(self):
        u''' correct sid '''
        response = rq_set(self.param,id = getConf('data','sid'),tempId=getConf('data','tem_id'), cycle=0, month=1, week=0, time="09:00", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u''' wrong sid '''
        response = rq_set(self.param,id = "abd",tempId=getConf('data','tem_id'), cycle=0, month=1, week=0, time="09:00", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    def test_c(self):
        u''' wrong tem_id '''
        response = rq_set(self.param,id = getConf('data','sid'),tempId='00000', cycle=0, month=1, week=0, time="09:00", rate=5, isSendSpockEmail=0)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_set()
    a.test_a()
    a.test_b()
    a.test_c()
        
    
