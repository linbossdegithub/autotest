'''
Created on 2018.10.26
@author: chenyongfa
'''
import json
import threading

import time

from websocket import WebSocketConnectionClosedException

from tools.tools import getConf


class HeartThread(threading.Thread):
    def __init__(self, wss=None,group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name, args=args, kwargs=kwargs,
                                  verbose=verbose)
        self.wss = wss
        self._stop = False

    def run(self):
        while True:
            if self._stop:
                return
            try:
                self.wss.ping()
            except WebSocketConnectionClosedException:
                print "close hearbeat"
                return
            print "::ping"
            time.sleep(15)

    def stop(self):
        self._stop = True