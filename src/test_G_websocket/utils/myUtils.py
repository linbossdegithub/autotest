import Queue
import json

import requests
import time
import websocket

from test_G_websocket.utils.recThread import RecThread
from tools.tools import getConf,setConf
from test_G_websocket.utils.heartThread import HeartThread


def connect(self,sn):
    q = Queue.Queue()
    self.queue = q
    url = getConf('constant', 'url')+'/api/index/websocketInfo'
    print url
    response = requests.get(url=url,verify=False)
    websocketUrl =  json.loads(response.text)['data']['websocketUrl']
    setConf('websocketdata','websocketurl',websocketUrl)
    print websocketUrl
    wss = websocket.create_connection(websocketUrl+'?appId=APPID&secret=SECRET&identifier='+sn+'&channel=1')
    self.wss = wss
    try:
        HeartThread(wss=wss).start()
        a = RecThread(sn=sn,queue=q,wss=wss)
        self.recThread = a
        a.start()
    except websocket.WebSocketConnectionClosedException:
        return
    time.sleep(2)