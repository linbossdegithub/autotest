#coding=utf-8
import unittest


from common.common import rq_saveScreenAlarmConf
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_saveScreenAlarmConf(ParametrizedTestCase):
    u''' alarmCycle:"0",alarmEmail:"",countryCode:"0",emailLanguage:"2",phone:"",sid:"4354",workTimeEnd:"22:00",workTimeStart:"06:00"'''
       
    def test_a(self):
        u''' correct params '''
        email = getConf('data','email')
        phone = getConf('data','phone')
        response = rq_saveScreenAlarmConf(self.param,alarmCycle="0",alarmEmail=email,countryCode="0",emailLanguage="1",phone=phone,sid=getConf('data', 'sid'),workTimeEnd="22:00",workTimeStart="06:00")
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
       
    # def test_b(self):
    #     u''' wrong sid '''
    #     response = rq_saveScreenAlarmConf(self.param,alarmCycle="0",alarmEmail="nova_chenyf@126.com",countryCode="0",emailLanguage="1",phone="17629228904",sid=0000,workTimeEnd="22:00",workTimeStart="06:00")
    #     print response
    #     u''' check '''
    #     self.assertTrue(response['status']==100000, 'this case is failed')

        
    def runTest(self):
        pass


