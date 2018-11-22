#coding=utf-8
'''
Created on 2018年11月15日

@author: linhuajian
'''
from requests_toolbelt import MultipartEncoder
from tools.tools import  getHeaders
import re
from common.common import rq_saveSystemConfig,rq_getEnterpriseInfo
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf,setConf
class Test_CorporateInfo(ParametrizedTestCase):
    def test_a_saveSystemConfig(self):
        u''' 保存企业信息参数： {"id":1002,"companyName":"test","companyAddress":"xian",
        "isCustom":0,"countryCode":"0","officialWebsite":"www.baidu.com",
        "phone":"182944477554","systemName":"NovaiCare","learnMoreUrl":"www.novaicare.com",
        "iconLogo":"https://care-qiniu-static.novaicare.com/favorite.ico",
        "systemLogo":"https://care-qiniu-static.novaicare.com/logo.png",
        "loginLogo":"https://care-qiniu-static.novaicare.com/login-logo.png",
        "emailLogo":"https://care-qiniu-static.novaicare.com/reportEmailLogo.png",
        "reportLogo":"https://care-qiniu-static.novaicare.com/reportLogo.png",
        "domain":"t-docker.novaicare.com","enable":1,"domainType":2,
        "copyright":"Copyright © 2007-2017 Novastar, Co. All Rights Reserved"}'''
        response=rq_getEnterpriseInfo(self.param)
        id=response['data']['id']
        response= rq_saveSystemConfig(self.param,id=id, companyName='test', companyAddress='xian',isCustom=0,countryCode='0',officialWebsite='www.baidu.com',phone=18294447754,systemName='NovaiCare',learnMoreUrl='www.novaicare.com',iconLogo='https://care-qiniu-static.novaicare.com/favorite.ico',systemLogo='https://care-qiniu-static.novaicare.com/logo.png',loginLogo='https://care-qiniu-static.novaicare.com/login-logo.png',emailLogo='https://care-qiniu-static.novaicare.com/reportEmailLogo.png',reportLogo='https://care-qiniu-static.novaicare.com/reportLogo.png',domain=re.sub(r'http://', "", re.sub(r'https://', "", getConf("constant", "url"))),enable=1,domainType=2,copyright='Copyright © 2007-2017 Novastar, Co. All Rights Reserved')
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b_saveSystemConfig(self):
        u'''企业信息自定义系统'''
        response=rq_getEnterpriseInfo(self.param)
        id=response['data']['id']
        response= rq_saveSystemConfig(self.param,id=id, companyName='test', companyAddress='xian',isCustom=1,countryCode='0',officialWebsite='www.baidu.com',phone=18294447754,systemName='NovaiCare',learnMoreUrl='www.novaicare.com',iconLogo='https://care-qiniu-static.novaicare.com/favorite.ico',systemLogo='https://care-qiniu-static.novaicare.com/logo.png',loginLogo='https://care-qiniu-static.novaicare.com/login-logo.png',emailLogo='https://care-qiniu-static.novaicare.com/reportEmailLogo.png',reportLogo='https://care-qiniu-static.novaicare.com/reportLogo.png',domain='Autotest.novaicare.com',enable=1,domainType=2,copyright='Copyright © 2007-2017 Novastar, Co. All Rights Reserved')
        print response
        u'check'
        self.assertTrue(response['status']==100000, 'this case is failed')
        
#     def test_c_saveSystemConfig(self):
#         u'''企业信息自定义系统上传log'''
#         files = {"loginLogo": open('./38.png', 'rb')}
#         print files
#         files = MultipartEncoder(files)
#         getHeaders()['Content-Type'] = files.content_type
#         print files
#         response= rq_saveSystemConfig(self.param,files=files)
#         print response
#         u'check'
#         self.assertTrue(response['status']==100000, 'this case is failed')
#         
        
    def runTest(self):
        pass 
        
if __name__ == '__main__':
    a = Test_CorporateInfo()
    a.test_a_saveSystemConfig()
    

    

