#coding=utf-8
import unittest
import requests
from common.common import asseetprint
from tools.tools import getConf,setConf

class Test_app(unittest.TestCase):
    
    def test_checkUserName(self):
        url = getConf("constant","url")+'/mobile/user/checkUserName'   
        data = '{"user":"'+getConf("constant", "user")+'"}'
        response = requests.post(url=url,data=data)
        result = asseetprint("checkUserName",response["code"],'10004')
        self.assertTrue(result)
        
    def test_checkPhone(self):
        u'''  countrycode   phonenumber'''
        url = getConf("constant","url")+'/mobile/user/checkPhone'   
        data = '{"countryCode":"'+getConf("data", "countryCode")+'","'+'phone":"'+getConf("data", "phone")+'"}'
        response = requests.post(url=url,data=data)
        result = asseetprint("checkPhone",response["code"],'10006')
        self.assertTrue(result)   
    
    def test_send(self):
        url = getConf("constant","url")+'/mobile/user/sms/send'   
        data = '{"countryCode":"'+getConf("data", "countryCode")+    '","language":"' + getConf("data", "language")+'","phone":"'+getConf("data", "phone")+'"}'
        response = requests.post(url=url,data=data)
        result = asseetprint("send",response["code"],'0')
        self.assertTrue(result)   
        
    def test_register(self):
        url = getConf("constant","url")+'/mobile/user/register '   
        data = '{ authCode":"433570",'+'"countryCode":"'+getConf("data", "countryCode")+'","'+'email":"'+getConf("data", "email")+  '","language":"' + getConf("data", "language")+'","password":"'+getConf("constant", "password")+ '","phone":"' +getConf("data", "phone")+'","username":"'+getConf("constant", "user")+'"}'
        response = requests.post(url=url,data=data)
        result = asseetprint("register",response["code"],'10012')
        self.assertTrue(result)      
       
    def test_login(self):
        url = getConf("constant","url")+'/mobile/user/login'   
        data = '{"password":"'+getConf("constant", "password")+'","User":"'+getConf("constant", "user")+'"}'
        response = requests.post(url=url,data=data)
        result = asseetprint("login",response["code"],'0')
        result1 = asseetprint("login",response["uid"],'3253')
        self.setConf("data","token",'response["token"]')
        self.setConf("data","uid",'response["uid"]')
        self.assertTrue(result and result1)  
        
    def test_label(self):
        url = getConf("constant","url")+'/mobile/user/label'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{"uid":"'+getConf("data", "uid")+'}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["list"]
        result = asseetprint("labe",response["code"],'0')
        self.assertTrue(result)     
        
    def test_detect(self):
        url = getConf("constant","url")+'/mobile/screen/detect'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{"uid":"'+getConf("data", "uid")+'}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["data"]
        result = asseetprint("detect",response["code"],'0')
        result1 = asseetprint("detect",response["status"],'1')
        self.assertTrue(result and result1)        
        
    def test_userScreen(self):
        url = getConf("constant","url")+'/mobile/screen/userScreen'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{"address":"'+getConf("data", "address")+' ","label":' +getConf("data", "label") +' ,"name":"' +getConf("data", "name")+'","status":'+getConf("data", "status")+',"uid":'+getConf("data", "uid")+'}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["screenList"]
        result = asseetprint("userScreen",response["code"],'0')
        result1 = asseetprint("userScreen",response["allStatus"],'[1,0,0]')
        self.assertTrue(result and result1)  

    def test_monitorData(self):
        url = getConf("constant","url")+'/mobile/screen/monitorData'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{"sid":"'+getConf("data", "sid")+'}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["alarmDetail"]
        print response["errorDetail"]
        print response["player"]
        result = asseetprint("monitorData",response["code"],'0')
        self.assertTrue(result)
        
    def test_cameraThumbnail(self):
        url = getConf("constant","url")+'/mobile/screen/cameraThumbnail'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{'+'"height":400,"width":400,'+'"sid":"['+getConf("data", "sid")+']}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["list"]
        result = asseetprint("cameraThumbnail",response["code"],'0')
        self.assertTrue(result)
        
    def test_cameraImage(self):
        url = getConf("constant","url")+'/mobile/screen/cameraImage'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{'+'"sid":"['+getConf("data", "sid")+']}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["list"]
        result = asseetprint("cameraImage",response["code"],'0')
        self.assertTrue(result)
        
    def test_Image(self):
        url = getConf("constant","url")+'/mobile/screen/Image'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{'+'"sid":"['+getConf("data", "sid")+']}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["list"]
        result = asseetprint("Image",response["code"],'0')
        self.assertTrue(result) 
        
    def test_thumbnail(self):
        url = getConf("constant","url")+'/mobile/screen/thumbnail'   
        headers = {'token': ' getConf("data", "token")'}
        data = '{'+'"sid":"['+getConf("data", "sid")+']}'
        response = requests.post(url=url,headers=headers,data=data)
        print response["list"]
        result = asseetprint("thumbnail",response["code"],'0')
        self.assertTrue(result)    
        
    def runTest(self):
        pass
    
if __name__ == "__main__":
    a = Test_app()
    a.test_checkUserName()
    a.test_checkPhone()
    a.test_send()
    a.test_register()
    a.test_login()
    a.test_label()
    a.test_detect()
    a.test_monitorData()
    a.test_cameraImage()
    a.test_cameraThumbnail()
    a.test_Image()
    a.test_thumbnail()
    
    
    
    
      
        