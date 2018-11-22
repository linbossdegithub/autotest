# coding=utf-8
import unittest
from ftplib import FTP

import datetime
from flask import json

from common.common import rq_getDeviceInfo, rq_cameraConfig, rq_realTime, rq_saveClientReportParamaterSet, \
    rq_saveReportScreenSet, rq_reportSetList, rq_deleteSetup
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf,setConf


class Test_bug(ParametrizedTestCase):
    def test_a(self):
        u''' 验证新建屏体的图片上传目录是否创建成功 '''
        response = rq_cameraConfig(self.param, sid=getConf('data', 'sid'),camera_id=getConf('data','camera_id3'))
        print response
        serverAddress = response['data']['serverAddress']
        userName = response['data']['userName']
        password = response['data']['password']
        storageDirectory = response['data']['storageDirectory']
        ftp = FTP()
        ftp.connect(serverAddress, 21)
        ftp.login(userName, password)
        dirlist = ftp.nlst()
        ftp.close()
        u''' check'''
        self.assertTrue(storageDirectory in dirlist, 'this case is failed')

    def test_b(self):
        u'''验证HTTPS是否可正常登陆'''
        username = getConf("constant",'user')
        password = getConf("constant",'password')
        url = getConf('constant','url')+'/login/loginCheck?username='+username+'&password='+password
        url.replace('http','https')
        headers = {}
        headers['Origin'] = getConf('constant','url')
        headers['Referer'] = getConf('constant','url')+'/login/index/redirect/%252F.html'
        headers["Cookie"] = getConf("data", "Cookie")
        headers["X-Requested-With"] ="XMLHttpRequest"
        result = self.param.request(method='get', url=url,headers=headers)
        print result.text
        self.assertTrue(json.loads(result.text)['status']==1,'this case is failed')

    def test_c(self):
        u'''验证接口中是否有智能模组的信息，间接验证icomet是否正常'''
        response = rq_realTime(self.param, sid=getConf("data", "sid"))
        print response
        u''' check '''
        print response['data']['smWorkTimeMax']
        print response['data']['smWorkTimeMin']
        self.assertTrue(response['data']['smWorkTimeMax'] == '100' and response['data']['smWorkTimeMin'] == '10', 'this case is failed')

    # def test_d(self):
    #     u'''验证客户定制报告是否能生成（但由于session验证不通过，绑定屏体接口不生效，暂未实现验证功能）'''
    #     response = rq_reportSetList(self.param)
    #     setupIds = []
    #     for li in response:
    #         setupIds.append(li['id'])
    #     print setupIds
    #     re = rq_deleteSetup(self.param,setupIds=setupIds)
    #     print 'delete result:'+ str(re)
    #     reportTime = (datetime.datetime.now() + datetime.timedelta(hours=-8, minutes=+1)).strftime('%H:%M')
    #     rq_saveClientReportParamaterSet(self.param,reportId='',reportPeriod=1,reportWeek=0,reportDate=1,reportTime=reportTime,reportEmail='nova_chenyf@126.com',reportEmailLanguage=0,reportName='interfacetest',clientName='interface')
    #     response = rq_reportSetList(self.param)
    #     for li in response:
    #         if li['cr_Name'] == 'interfacetest':
    #             setConf('data','reportid',li['id'])
    #     response = rq_saveReportScreenSet(self.param,reportSetId =getConf('data','reportId'),screenId=getConf('data','sid'))
    #     print getConf('data','reportId')
    #     self.assertTrue(response['result'])




    def runTest(self):
        pass


if __name__ == '__main__':
    a = Test_bug()
    a.test_a()

