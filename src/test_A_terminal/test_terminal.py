#coding=utf-8
import unittest
from time import sleep

import requests

from common.common import asseetprint
from tools.tools import getConf


class Test_terminal(unittest.TestCase):
    
    def test_aregister(self):

        url = getConf("constant","url")+'/api/index/register'
        data = '{"User":"'+getConf("constant", "user")+'","Mac":"'+getConf("constant", "mac")+'","IsReregistering":true,"RegistationInfos":[{"sn_num":"'+getConf("constant", "sn")+'","led_name":"'+getConf("constant", "led_name")+'","led_width":128,"led_height":128,"Latitude":0,"Longitude":0,"card_num":"1+1+1","mac":"'+getConf("constant", "mac")+'","UserID":"","IsReregistering":true,"ControlSystem":1,"IsSupperDisplay":false,"BasicSNList":[]}]}'
        response = requests.post(url=url,data=data,verify = False)
        result = asseetprint("test_register",response.text,'3')
        sleep(2)
        self.assertTrue(result)
        
    
    def test_heartbeat(self):
        url = getConf("constant","url")+'/api/index/heartbeat'
        data = '{"Identifier":"'+getConf("constant", "mac")+'+'+getConf("constant", "sn")+'","Timestamp":"1521007106","SystemVersion":"2.6.1707.10101","SyncInfos":[{"SyncMark":"-1","Type":1},{"SyncMark":"-1","Type":3},{"SyncMark":"-1","Type":4},{"SyncMark":"-1","Type":7},{"SyncMark":"-1","Type":8},{"SyncMark":"1515398794","Type":6},{"SyncMark":"1515398862","Type":2},{"SyncMark":"1508228308","Type":5}]}'
        response = requests.post(url=url,data=data,verify = False)
        print response.text
        result = eval((response.text).replace("null","None"))['result']
        result = asseetprint("test_heartbeat",str(result),'6')
        self.assertTrue(result)
    
    def test_getSreen(self):
        url = getConf("constant","url")+'/api/index/getScreen'
        data = '[{"mac":"'+getConf("constant", "mac")+'","sn":""}]'
        response = requests.post(url=url,data=data,verify = False)
        print response.text
        result = asseetprint("test_getSreen",response.text,getConf("constant", "mac"))
        self.assertTrue(result)
    
    
    def test_bupdateConf(self):
        url = getConf("constant","url")+'/api/index/updateConf'
        data = '{"mac":"'+getConf("constant", "mac")+'","sn_num":"'+getConf("constant", "sn")+'","led_height":2048,"led_width":2048,"card_num":"1+64+64","IsSupportPointDetect":true,"IsSupportAutoBrightness":true,"PointCount":12582912,"IsSupperScreen":false}'
        response = requests.post(url=url,data=data,verify = False)
        result1 = asseetprint("test_updateConf",response.text,'7')
        result2 = asseetprint("test_updateConf",response.text,'8')
        self.assertTrue(result1 or result2)
        
        
    def test_cSpotCheck(self):
        url = getConf("constant","url")+'/api/SpotCheck/index'
        data = '{"Id":"'+getConf("constant", "mac")+'+'+getConf("constant", "sn")+'","Timestamp":"1522122241","Result":true,"IsSupportVirtualRed":false,"TotalPoint":6144,"UnitCount":1,"SpotInspectionBoxList":[{"Position":"0-3-0","BoxTotalPoint":6144,"SpotInspectionUnitList":[{"UnitTotalPoint":6144,"AllErrorPointNumner":6144,"RedPointErrorNumber":2048,"BluePointErrorNumber":2048,"GreenPointErrorNumber":2048,"VirtualRedPointErrorNumber":0}]}]}'
        response = requests.post(url=url,data=data,verify = False)
        result = asseetprint("test_SpotCheck",response.text,'13')
        self.assertTrue(result)
        
        
    def test_brightlog(self):
        url = getConf("constant","url")+'/api/brightness/brightlog'
        data = '{"Id":"'+getConf("constant", "mac")+'+'+getConf("constant", "sn")+'","Timestamp":"1523942525","BrightnessValue":51,"OperationType":0,"Result":1}'
        response = requests.post(url=url,data=data,verify = False)
        result = asseetprint("test_brightlog",response.text,'13')
        self.assertTrue(result)
    
    def test_index(self):#伴随心跳接口一起
        url = getConf("constant","url")+'/api/SyncInfo/index'
        data = '{"Sn":"'+getConf("constant", "mac")+'+'+getConf("constant", "sn")+'","SyncDatas":[{"SyncType":1,"SyncParam":0,"SyncContent":"","Datestamp":"-1"},{"SyncType":3,"SyncParam":0,"SyncContent":"","Datestamp":"-1"},{"SyncType":4,"SyncParam":0,"SyncContent":"","Datestamp":"-1"},{"SyncType":5,"SyncParam":0,"SyncContent":"","Datestamp":"-1"},{"SyncType":6,"SyncParam":0,"SyncContent":"","Datestamp":"-1"},{"SyncType":2,"SyncParam":1,"SyncContent":"","Datestamp":"0"}]}'
#         data = '{"sn":"'+getConf("constant", "mac")+'+'+getConf("constant", "sn")+'","Timestamp":"1521010589","BrightnessValue":51,"OperationType":0,"Result":1}'
        response = requests.post(url=url,data=data,verify = False)
        result = asseetprint("test_index",response.text,"SyncDatas")
        self.assertTrue(result)
    
    def test_updateScreenStatus(self):
        url = getConf("constant","url")+'/api/index/UpdateScreenStatus'
        data = '{"Timestamp":"1521013940","Status":[{"Identifier":"'+getConf("constant", "mac")+'+'+getConf("constant", "sn")+'","Type":0}]}'
        response = requests.post(url=url,data=data,verify = False)
        result = asseetprint("test_updateScreenStatus",response.text,'"cache":1')
        self.assertTrue(result)
        
    
    def test_monitorData(self):
        #nomal "H4sIAAAAAAAEAJXTsWoDMQwG4HfxejFIsizJtyV3yZK9S+nQIVvXDqXOu1cHhdwlcKDBg/k/2TJY77/pevtJY6IuvXRAACBfApAO6e3z6/vmIaT74QF1DXUH2hraBspWTp0fsviado59whjBFMElgjmCawRLBGsEWwS3CD5G8CmCpwieI/gcwZcdXH2W6vY/15eZwlXBqR87eMEq1sFYwFSNeGBQNEZtNExjNqkEIoYCmZClMTUVGOYxIzeqfnFjhowgzYoPCBIM5/8QsRqgZPPzxOlSePEMK6giMTTxzSILSSmy6hKXcd52CZt4fo6zP/LjDzbyBuxjBAAA"
        url = getConf("constant","url")+'/api/index/monitorData'
        data = '{"Identifier":"'+getConf("constant", "mac")+'+'+getConf("constant", "sn")+'","IdentifierClass":1,"Timestamp":"636566072110807453","SequenceNumber":"","DataPointCollection":"H4sIAAAAAAAAA53UsW6EMAwG4HfJyiHZjuM4bHfALd27VB063Na1Q9Xcu9dUlS6hEpI7eID/cyAR5uUrPN0+wxSoSo0VEADISgDCKTy/vX/cLIRwPz1gbmE+gNpC7aD0cq78kNFqPlh2h9GDyYOjB7MHJw8WD84erB5cPPjswRcPnj148eDVg68HONkspf57Tn9mCpuGSz1XsIYmzoOygOasxANDRmXMhYZ5GlUSgYiiwEjIUphKFhiWaUQulOzBhRlGBCkabUCQYFh/Q8SkgDKqrSdGt8arZZggZySGInaxyUgSozRvOdd1P6bbtha7s/5Utz2A/7c2nbj9Q/qj6eNlH492sq/fCC+sXdgEAAA=","SoftwareVersion":"4.9.1707.14801"}'
        header = {'EnablingCompression':'1'}
        response = requests.post(url=url,headers=header,data=data,verify = False)
        result = asseetprint("test_monitorData",response.text,'6')
        self.assertTrue(result)
        
    def runTest(self):
        pass
    
      
if __name__ == "__main__":
    a = Test_terminal()
#     a.test_aregister()
    a.test_heartbeat()
#     a.test_monitorData()
#     a.test_bupdateConf()
#     a.test_cSpotCheck()
        
        
        