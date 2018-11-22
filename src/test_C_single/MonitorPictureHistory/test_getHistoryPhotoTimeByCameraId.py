#coding=utf-8
import unittest

from common.common import rq_getHistoryPhotoTimeByCameraId
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_getHistoryPhotoTimeByCameraId(ParametrizedTestCase):
    def test_a(self):
        u''' 待完善 '''
        response = rq_getHistoryPhotoTimeByCameraId(self.param,cameraId=getConf("data","camera_id1"))
        print response
        u''' check '''
        self.assertTrue(response["status"]==100001, "this case is failed")
    def test_b(self):
        u''' 待完善 '''
        response = rq_getHistoryPhotoTimeByCameraId(self.param,cameraId="' or 1='1")
        print response
        u''' check '''
        self.assertTrue(response["status"]==100001, "this case is failed")
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_getHistoryPhotoTimeByCameraId()
    a.test_a()
    a.test_b()

