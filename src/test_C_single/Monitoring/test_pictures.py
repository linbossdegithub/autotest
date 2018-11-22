#coding=utf-8

from common.common import  rq_pictures, rq_enableSet
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_pictures(ParametrizedTestCase):
    def setUp(self):
        rq_enableSet(self.param,sid=getConf("data","sid"),camera_id=getConf('data', 'camera_id1'),enable=True)
       
    u'''参数：sid grid ''' 
    def test_a(self):

        u'''正确的sid grid=0'''
        sid = getConf("data","sid")
        response = rq_pictures(self.param,sid=sid,grid=0)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000 and len(response["data"]["screens"])!=0,u"this case is failed")
    def test_b(self):
        u'''正确的sid grid=1'''
        sid = getConf("data","sid")
        response = rq_pictures(self.param,sid=sid,grid=1)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000 and len(response["data"]["screens"])!=0,u"this case is failed")
        
    def test_c(self):
        u'''正确的sid grid="1"'''
        sid = getConf("data","sid")
        response = rq_pictures(self.param,sid=sid,grid="1")
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000 and len(response["data"]["screens"])!=0,u"this case is failed")
        
    def test_d(self):
        u'''正确的sid 不传grid'''
        sid = getConf("data","sid")
        response = rq_pictures(self.param,sid=sid)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000 and len(response["data"]["screens"])!=0,u"this case is failed")
        
    def test_e(self):
        u'''不传sid 不传grid'''
        response = rq_pictures(self.param,)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100001,u"this case is failed")
        
    def test_f(self):
        u'''传错误sid=00000 grid=0'''
        response = rq_pictures(self.param,sid="00000",grid=0)
        print response
        u''' check'''
        self.assertTrue(response["status"]==100000 and len(response["data"]["screens"])==0,u"this case is failed")
        
    
        
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_pictures()
    a.test_a()
    a.test_b()
    a.test_c()
    a.test_d()
    a.test_e()
    a.test_f()
