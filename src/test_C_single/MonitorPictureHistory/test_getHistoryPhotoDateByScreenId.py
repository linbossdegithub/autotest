#coding=utf-8
import unittest

from common.common import rq_getHistoryPhotoDateByScreenId
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf



class Test_getHistoryPhotoDateByScreenId(ParametrizedTestCase):
    
    u'''参数：
        cameraId: 7758
        endTime: 
        orderName: dir_time
        orderType: desc
        pageSize: 10
        sid: 4329
        startTime:  '''
    
    def test_a(self):
        u''' 只传 cameraId1 '''
        response = rq_getHistoryPhotoDateByScreenId(self.param,cameraId=getConf("data","camera_id1"))
        u''' check '''
        print response
        self.assertTrue(response["status"]==100000, "this case is failed")
        
    def test_b(self):
        u''' 传 cameraId2  错误的sid '''
        response = rq_getHistoryPhotoDateByScreenId(self.param,cameraId=getConf("data","camera_id2"),sid="00000")
        u''' check '''
        print response
        self.assertTrue(response["status"]==100000, "this case is failed")
    
    def test_c(self):
        u''' 传 错误的 cameraId'''
        response = rq_getHistoryPhotoDateByScreenId(self.param,cameraId=1111111111)
        u''' check '''
        print response
        self.assertTrue(response["status"]==100001, "this case is failed")
    
    
        
    def runTest(self):
        pass
    
    
if __name__ == "__main__":
    a = Test_getHistoryPhotoDateByScreenId()
    a.test_c()

