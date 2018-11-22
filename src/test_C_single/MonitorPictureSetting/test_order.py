#coding=utf-8
import unittest
from common.common import rq_order
from parametrizedTestCase import ParametrizedTestCase
from tools.tools import getConf


class Test_order(ParametrizedTestCase):
    
    u''' params camera_id:7793 orders: [{id: 7794, order: 1}, {id: 7793, order: 2}, {id: 7795, order: 3}, {id: 7796, order: 4}] '''
    def test_a(self):
        u'''correct params'''
        
        one = {}
        one['id'] =  getConf('data', 'camera_id1')
        one['order'] = 1
        two = {}
        two['id'] =  getConf('data', 'camera_id2')
        two['order'] = 2
        three = {}
        three['id'] =  getConf('data', 'camera_id3')
        three['order'] = 3
        four = {}
        four['id'] =  getConf('data', 'camera_id4')
        four['order'] = 4
        
        orders = []
        orders.append(one)
        orders.append(two)
        orders.append(three)
        orders.append(four)
        
        response = rq_order(self.param,camera_id=getConf('data','camera_id1'),orders=orders)
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    def test_b(self):
        u'''no camera_id'''
        
        one = {}
        one['id'] =  getConf('data', 'camera_id1')
        one['order'] = 1
        two = {}
        two['id'] =  getConf('data', 'camera_id2')
        two['order'] = 2
        three = {}
        three['id'] =  getConf('data', 'camera_id3')
        three['order'] = 3
        four = {}
        four['id'] =  getConf('data', 'camera_id4')
        four['order'] = 4
        
        orders = []
        orders.append(one)
        orders.append(two)
        orders.append(three)
        orders.append(four)
        
        response = rq_order(self.param,orders=orders)
        print response
        u''' check '''
        self.assertTrue(response['status']==100000, 'this case is failed')
        
    
        
    def runTest(self):
        pass
if __name__ == "__main__":
    a = Test_order()
    a.test_b()


