#coding=utf-8
import datetime
import unittest

from common.common import rq_detail, rq_settingDetail, rq_screenDetail, rq_settingEdit, rq_screenEdit, rq_history, \
    rq_setEncrypt
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_PerodicInspectionReport(ParametrizedTestCase):
    
    def test_a_detail(self):
        u''' params currentPage: 1  orderName:s_name  orderType:desc  pageSize: 10'''
        response = rq_detail(self.param,currentPage=1,orderName='s_name',orderType='desc' ,pageSize=10)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
    
    # def test_b_detail(self):
    #     u''' params currentPage: 1  orderName: aaaaaa  orderType: desc  pageSize: 10'''
    #     response = rq_detail(self.param,currentPage=1,orderName="aaaaaa",orderType='desc' ,pageSize=10)
    #     print response
    #     u'check'
    #     self.assertTrue(response['status']==100001, 'this case is failed')
        
        
    def test_c_settingDetail(self):
        response = rq_settingDetail(self.param,)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_d_screenDetail(self):
        response = rq_screenDetail(self.param,)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_e_settingEdit(self):
        u''' reportDate:"1"  reportEmail:"nova_chenyf@126.com"  reportLanguage:"1"  reportPeriod:"1"  reportTime:"07:13"  reportTimeSecond:"00:00"  reportWeek:"0"'''
        reportTime=(datetime.datetime.now()+datetime.timedelta(hours=-8,minutes=+1)).strftime('%H:%M')
        response = rq_settingEdit(self.param,reportDate="1",reportEmail=getConf('data','email'),reportLanguage="1",reportPeriod="1",reportTime=reportTime,reportWeek="0")
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_f_screenEdit(self):
        u''' screenId:[4354]'''
        print getConf('data','sid')
        sid = rq_setEncrypt(self.param,data=getConf('data','sid'))
        print sid
        response = rq_screenEdit(self.param,screenId=sid)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_g_history(self):
        u''' currentPage: 1   orderName: reportTime  orderType: desc   pageSize: 10'''
        response = rq_history(self.param,currentPage=1,orderName='reportTime',orderType='desc',pageSize=10)
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    
    def test_h_screenEdit(self):
        u''' wrong screenId:'''
        response = rq_screenEdit(self.param,screenId=['00000'])
        print response
        u'check'
        self.assertTrue(response['status']==100001, 'this case is failed')
        
    
        
        
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_PerodicInspectionReport()
    # a.test_a_detail()
    # a.test_b_detail()
    # a.test_c_settingDetail()
    # a.test_d_screenDetail()
    # a.test_e_settingEdit()
    # a.test_f_screenEdit()
    # a.test_g_history()
    # a.test_h_screenEdit()
        
    

