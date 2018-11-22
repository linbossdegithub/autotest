#coding=utf8
'''
Created on 2018.10.26
@author: chenyongfa
'''
import json
import unittest

import time

from test_G_websocket.utils.myUtils import connect
from tools.tools import getConf


class Test_websocket(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sn = getConf('websocketdata','websocketSn').upper()
        mac = getConf('websocketdata', 'websocketMac')
        cls.sn = sn
        cls.mac = mac
        connect(cls,sn)
    def test_a_register(self):
        self.recThread.setNum(3)
        userName = getConf('constant','user')
        data = getConf('websocketdata', 'register')
        data = json.loads(data)
        data['content']['body']['Mac'] = self.mac
        data['content']['body']['RegistationInfos'][0]['mac'] = self.mac
        data['content']['body']['RegistationInfos'][0]['sn_num'] = self.sn + "-00"
        data['content']['body']['RegistationInfos'][0]['UserID'] = 'Taurus-' + self.sn + "-00"
        data['content']['body']['RegistationInfos'][0]['led_name'] = getConf("websocketdata","websocketName").upper()
        data['content']['body']['User'] = userName
        print "register::"+str(data)
        self.wss.send(json.dumps(data))
        time.sleep(1)
        info =  self.queue.get()
        print info
        self.assertTrue(str(json.loads(info)['content']['data']['Result'])=='3',"register failed!!")

    def test_b_bind(self):
        self.recThread.setNum(5)
        data = getConf('websocketdata', 'bind')
        data = json.loads(data)
        data['content']['header']['playerIdentifier'] = self.mac + '+' + self.sn + "-00"
        print data
        self.wss.send(json.dumps(data))
        time.sleep(1)
        info = json.loads(self.queue.get())
        print info
        self.assertTrue(info['content']['status']==10000000,"bind failed")

    def test_c_updateConf(self):
        self.recThread.setNum(6)
        data = getConf('websocketdata', 'updateConf')
        data = json.loads(data)
        data['content']['body']['sn_num'] = self.sn + "-00"
        data['content']['body']['mac'] = self.mac
        data['content']['body']['s_name'] = 'Taurus' + self.sn + "-00"
        data = json.dumps(data)
        self.wss.send(data)
        time.sleep(1)
        info = json.loads(self.queue.get())
        print info
        self.assertTrue(info['content']['status'] == 10000000, "updateConf failed")

    def test_d_minitorData(self):
        self.recThread.setNum(7)
        data = json.loads(getConf('websocketdata', 'monitorData'))
        data['content']['body']['Identifier'] = self.mac + "+" + self.sn + "-00"
        data = json.dumps(data)
        self.wss.send(data)
        time.sleep(1)
        info = json.loads(self.queue.get())
        print info
        self.assertTrue(info['content']['status'] == 10000000, "minitorData failed")

    def test_e_index(self):
        data1 = json.loads(getConf('websocketdata', 'index'))
        data1['content']['body']['terminal_identifier'] = self.sn
        data1 = json.dumps(data1)
        self.wss.send(data1)
        time.sleep(1)

    def test_f_brightlog(self):
        data = json.loads(getConf('websocketdata', 'brightlog'))
        data['content']['body']['terminal_identifier'] = self.sn
        data1 = json.loads(getConf('websocketdata', 'brightlog1'))
        data1['content']['body']['terminal_identifier'] = self.sn
        data = json.dumps(data)
        data1 = json.dumps(data)
        self.wss.send(data)
        self.wss.send(data1)
        time.sleep(1)


    def test_g_SpotCheck(self):
        self.recThread.setNum(10)
        data = json.loads(getConf('websocketdata', 'SpotCheck'))
        data['content']['body']['Id'] = self.mac + "+" + self.sn + "-00"
        data = json.dumps(data)
        self.wss.send(data)
        time.sleep(1)
        info = json.loads(self.queue.get())
        print info
        self.assertTrue(info['content']['status'] == 10000000, "SpotCheck failed")

    @classmethod
    def tearDownClass(cls):
        cls.wss.abort()
        # self.wss.close()


    def runTest(self):
        pass

if __name__ == "__main__":
    a = Test_websocket()
    a.setUp()
    # a.test_a_register()
    # a.test_b_bind()
    # a.test_c_updateConf()
    a.test_d_minitorData()
    a.test_d_minitorData()
    a.test_d_minitorData()
    a.test_d_minitorData()
    a.tearDown()