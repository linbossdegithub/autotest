# coding=utf-8
import unittest

from tools.tools import getConf

from common.commonapp import rq_cameraImage

class Test_CameraImage(unittest.TestCase):
    u''' sid'''

    def test_a(self):
        u''' correct params '''
        li = [getConf('data','sid')]
        response = rq_cameraImage(sid=li)
        print response
        u'check'
        self.assertTrue(response['code'] == 0 , 'this case is failed')
    def runTest(self):
        pass
if __name__ == '__main__':
    a = Test_CameraImage()
    a.test_a()

