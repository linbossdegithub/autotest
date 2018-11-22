#coding=utf-8

from common.common import rq_save_selects, rq_enableSet
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf

import unittest
class Test_saveselects(ParametrizedTestCase):
    def setUp(self):
        rq_enableSet(self.param,sid=getConf("data","sid"),camera_id=getConf('data', 'camera_id1'),enable=True)

    u''' {selects: [{sid: 4329, name: "chenyongfa", tags: "", sort: 0, status: true}]} '''
    def test_a(self):
        u'''不传参数'''
        response = rq_save_selects(self.param)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100001,u"this case is failed")
        
    def test_b(self):
        u'''传 sid name'''
        dct = {}
        dct["sid"] = getConf("data", "sid")
        dct["name"] = getConf("constant", "led_name")
        
        li = []
        li.append(dct)
        
        response = rq_save_selects(self.param,selects=li)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000,u"this case is failed")
        
    def test_c(self):
        u'''传 错误的sid'''
        dct = {}
        dct["sid"] = 111111
        li = []
        li.append(dct)
        
        response = rq_save_selects(self.param,selects=li)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000,u"this case is failed")
    
    def runTest(self):
        pass
    
if __name__ == "__main__":
    a = Test_saveselects()
    a.test_a()
    a.test_b()
    a.test_c()
    a.test_c()
    a.test_c()