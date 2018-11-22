'''
Created on 2018.10.26
@author: chenyongfa
'''
import json
import threading

from websocket import WebSocketConnectionClosedException

from tools.tools import getConf


class RecThread(threading.Thread):
    def __init__(self, sn=None,queue=None,wss=None,num=None,group=None, target=None, name=None, 
        args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name, args=args, kwargs=kwargs, verbose=verbose)
        self.sn = sn
        self.queue = queue
        self.wss = wss
        self.num = num
        self._stop = False
        
    def run(self):
        while True:
            if self._stop:
                return
            try:
                data = self.wss.recv()
            except WebSocketConnectionClosedException:
                print "close recThread"
                return
            info = json.loads(data)
            if not data:
                print self.num+":data wei kong le"
                break
            if self.num:
                if str(info['requestId']) == str(self.num):
                    self.queue.put(data)
                
            else:
                a = str(info['command'])
                data = json.loads(getConf("websocketdata",a))
                data['requestId'] = info['requestId']
                data['content']['body']['terminal_identifier'] = self.sn
                self.wss.send(json.dumps(data))

    def setNum(self,num):
        self.num = num

    def stop(self):
        self._stop=True  