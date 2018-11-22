#coding=utf-8
import unittest


from common.common import rq_saveScreenInfo
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_saveScreenInfo(ParametrizedTestCase):
    u''' address:"" isSummerTime:"0",latitude:"0.000000",longitude:"0.000000",sName:"chenyongfa",sid:"4354",tagAuthority:1,tids:[],timeZone:"8"'''
       
    def test_b(self):
        u''' correct params '''
        response = rq_saveScreenInfo(self.param,address="",isSummerTime="0",latitude="0.000000",longitude="0.000000",sName=getConf('constant','led_name'),sid=getConf('data', 'sid'),tagAuthority=1,tids=[],timeZone="8")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
       
    def test_a(self):
        u''' wrong sid '''
        response = rq_saveScreenInfo(self.param,address="",isSummerTime="0",latitude="0.000000",longitude="0.000000",sName="chenyongfa",sid='00000',tagAuthority=1,tids=[],timeZone="9")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def runTest(self):
        pass


