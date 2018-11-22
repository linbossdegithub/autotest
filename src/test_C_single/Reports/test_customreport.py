#coding=utf-8
'''
Created on 2018��10��18��

@author: Administrator
'''
import time
import datetime
import unittest
from common.common import rq_customreportdelete,rq_customreportedit,rq_customreportsave,rq_setEncrypt,rq_getcustomreport
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf,setConf
import re

class Test_Customreport(ParametrizedTestCase):
    def test_a_delete(self):
        u'''  删除客户定制报告 {"ids":[ ]}'''
        customreport_editlist= rq_getcustomreport(self.param,b=' b'  )
        print customreport_editlist
        idds=[]
        for v in customreport_editlist['data']['reportList']:
            idds.append(v['id'])
        print idds
        response = rq_customreportdelete(self.param,ids=idds)
        print response
        time.sleep(1)
        u'check'
        if(response['status']!=100000):
            print '删除失败'
        
            
        
    def test_b_save(self):

        u''' 配置为每天发送客户定制报告params {"reportId":"   reportName":"    clientName":"     reportPeriod":"
          reportWeek":"    reportDate":"    reportEmailLanguage":"      reportTime":" 
          reportEmail '''
        print getConf('data','email')
        response = rq_customreportsave(self.param,reportId="",reportName='autotest',clientName='autotest '  ,  reportPeriod= 1 ,reportWeek=1,   reportDate=1, reportEmailLanguage =1, reportTime= str((datetime.datetime.now()+datetime.timedelta(hours=-8,minutes=2)).strftime('%H:%M')),reportEmail =getConf('data','email')  )
        setConf("data","customreportid",re.sub(r'\D', "", str(response['data'])))
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')

        
    def test_c_edit(self):
        u''' 客户定制报告关联屏体{ "screenIds":"","reportId":242}'''
#         sid = rq_setEncrypt(self.param,data=getConf('data','sid'))
#         print sid
        response = rq_customreportedit(self.param,screenIds=getConf('data','sid'),reportId=getConf('data','customreportid'))
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_d_save(self):
        u''' 配置为每周发送客户定制报告params {"reportId":"   reportName":"    clientName":"     reportPeriod":"
          reportWeek":"    reportDate":"    reportEmailLanguage":"      reportTime":" 
          reportEmail '''
        
        response = rq_customreportsave(self.param,reportId='',reportName='autotestweek',clientName='autotest '  ,  reportPeriod= 2 ,reportWeek=datetime.datetime.now().weekday()+1,   reportDate=1, reportEmailLanguage =1 , reportTime= str((datetime.datetime.now()+datetime.timedelta(hours=-8,minutes=2)).strftime('%H:%M')),reportEmail = getConf('data','email') )
        setConf("data","customreportid",re.sub(r'\D', "", str(response['data'])))
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
    def test_e_edit(self):
        u''' 每周客户定制报告关联屏体{ "screenIds":"","reportId":242}'''
#         sid = rq_setEncrypt(self.param,data=getConf('data','sid'))
#         print sid
        response = rq_customreportedit(self.param,screenIds=getConf('data','sid'),reportId=getConf('data','customreportid'))
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_f_save(self):
        u''' 配置为每月发送客户定制报告params {"reportId":"   reportName":"    clientName":"     reportPeriod":"
          reportWeek":"    reportDate":"    reportEmailLanguage":"      reportTime":" 
          reportEmail '''
        
        response = rq_customreportsave(self.param,reportId='',reportName='autotestmoth',clientName='autotest '  ,  reportPeriod= 3 ,reportWeek=1,   reportDate=datetime.datetime.now().strftime('%d'), reportEmailLanguage =2 , reportTime= str((datetime.datetime.now()+datetime.timedelta(hours=-8,minutes=2)).strftime('%H:%M')),reportEmail =getConf('data','email')  )
        setConf("data","customreportid",re.sub(r'\D', "", str(response['data'])))
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
    def test_g_edit(self):
        u''' 每月客户定制报告关联屏体{ "screenIds":"","reportId":242}'''
#         sid = rq_setEncrypt(self.param,data=getConf('data','sid'))
#         print sid
        response = rq_customreportedit(self.param,screenIds=getConf('data','sid'),reportId=getConf('data','customreportid'))
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_Customreport()
    a.test_a_delete()
    

    

