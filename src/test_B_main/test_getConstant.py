#coding=utf-8
import hashlib

from common import common
from common.common import rq_getScreenList
from common.commonapp import rq_rlogin
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf, setConf
import unittest

class Test_getConstant(ParametrizedTestCase):
    def test_a(self):
        u'''获取并保存sid'''
        r = self.param
        sid = ''
        result = rq_getScreenList(r,PageSize='100')
        for li in result['data']['ScreenList']:
            if li['ScreenName'] == getConf('constant', 'led_name'):
                sid = li['Sid']
        if not sid:
            raise Exception("screen not exits")
            unittest.main(failfast=True)
        setConf("data","sid",sid)

        u'''获取并保存camera_id'''
        sid = str(getConf("data","sid"))
        rp_cameras = common.rq_cameras(r,sid=sid)
        setConf("data", "camera_id1", rp_cameras["data"][0]["id"])
        setConf("data", "camera_id2", rp_cameras["data"][1]["id"])
        setConf("data", "camera_id3", rp_cameras["data"][2]["id"])
        setConf("data", "camera_id4", rp_cameras["data"][3]["id"])

    def test_b(self):
        u'''make username and password for ftp'''
        # rq_rlogin(password=getConf("constant", "password"), username=getConf("constant", "user"))
        mix_string = hashlib.md5(getConf('constant','user')).hexdigest()
        user_e = mix_string[0:8]
        setConf('constant','user_e',user_e)
        password_e = mix_string[9:17]
        setConf('constant', 'password_e', password_e)
