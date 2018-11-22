# coding=utf-8
import unittest
from ftplib import FTP

import datetime
from flask import json

from common.common import *
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf,setConf
import time


class Test_bug2(ParametrizedTestCase):
    def test_a(self):
        u''' 验证2分钟内能否将图片上传 '''
        #打开摄像机
        print 'open camera'
        rq_enableSet(self.param,sid=getConf("data","sid"),camera_id=getConf('data', 'camera_id1'),enable=True)
        #获取ftp配置
        print 'get config for ftp'
        response = rq_cameraConfig(self.param, sid=getConf('data', 'sid'),camera_id=getConf('data','camera_id1'))
        serverAddress = response['data']['serverAddress']
        userName = response['data']['userName']
        password = response['data']['password']
        remotepath = response['data']['storageDirectory']
        #配置摄像机
        print ''
        ftp = FTP()
        ftp.connect(serverAddress, 21)
        ftp.login(userName, password)
        #上传图片
        fp = open('./chen.jpg', 'rb')
        nowTime = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
        filename = nowTime + ".jpg"
        file = remotepath + "/" + filename
        ftp.storbinary('STOR ' + file, fp, 1024)
        ftp.close()
        #检查图片是否上传至七牛
        for i in range(200):
            print 'check %s'%i
            time.sleep(5)
            response = rq_checkCameraSet(self.param, sid=getConf("data", "sid"),camera_id=getConf("data", "camera_id1"))
            if response['status'] != 100000:
                raise Exception("checkCameraSet failed")
            if response['data']['code'] == 1:
                print 'pictrue upload successful'
                return
        raise Exception('no pictrue upload in four munites ')

    def test_b(self):
        u'''验证现场画面图片是否能展示'''

        #现场画面选择屏体
        di = {}
        di['sid'] = getConf('data','sid')
        di['name'] = getConf('constant','led_name')
        di['tags'] = ''
        di['sort'] = 0
        di['status'] = True
        li = []
        li.append(di)
        result = rq_save_selects(self.param,selects = li)
        print result
        result = rq_pictures(self.param,grid=1,sid = getConf('data','sid'))
        url =  result['data']['screens'][0]['img'][0]['url']
        print url
        code = requests.get(url=url,verify = False).status_code
        if code==200:
            print 'Monitoring picture show success'
        else:
            raise Exception('Monitoring picture show failed')
