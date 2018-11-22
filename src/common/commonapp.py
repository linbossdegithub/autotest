#coding=utf-8


import requests
#转化为json
from flask import json
from tools.tools import  getHeaders, getConf,setConf,getHeadersE


def rq_checkUserName(**kwarg):
    u'''检查用户名是否已注册'''
    url = getConf("constant","url")+'/mobile/user/checkUserName'   
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))
def rq_checkPhone(**kwarg):
    u'''检查手机号是否已注册'''
    url = getConf("constant","url")+'/mobile/user/checkPhone'    
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_send(**kwarg):
    u'''发送手机验证码'''
    url = getConf("constant","url")+'/mobile/sms/send'    
#     headers = getHeaders()
    response = requests.post(url=url,json=kwarg,verify = False)
    print response.text
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_register(**kwarg):
    u'''注册'''
    url = getConf("constant","url")+'/mobile/user/register '  
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    print response.text
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_login(**kwarg):
    u'''登录'''
    url = getConf("constant","url")+'/mobile/user/login'     
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))
def rq_rlogin(**kwarg):
    u'''正确登录'''
    url = getConf("constant","url")+'/mobile/user/login'     
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    aa=response.text
    ss=eval(aa)
    setConf("data","token",ss["token"])
    setConf("data","uid",ss["uid"])
    return eval((response.text).replace("false","False").replace("true","True"))


def rq_label(**kwarg):
    u'''获取用户标签列表'''
    url = getConf("constant","url")+'/mobile/user/label'   
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_labelE(**kwarg):
    u'''获取用户标签列表,错误token'''
    url = getConf("constant","url")+'/mobile/user/label'   
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_detect(**kwarg):
    u'''获取单个屏体点检数据'''
    url = getConf("constant","url")+'/mobile/screen/detect'   
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    strdict=json.loads(response.text)
#     return eval((response.text).replace("false","False").replace("true","True"))
    return strdict
def rq_detectE(**kwarg):
    u'''获取单个屏体点检数据,错误token'''
    url = getConf("constant","url")+'/mobile/screen/detect'   
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    strdict=json.loads(response.text)
#     return eval((response.text).replace("false","False").replace("true","True"))
    return strdict

def rq_userScreen(**kwarg):
    u'''获取屏体列表'''
    url = getConf("constant","url")+'/mobile/screen/userScreen'    
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    strdict=json.loads(response.text)
#     return eval((response.text).replace("false","False").replace("true","True"))
    return strdict
def rq_userScreenE(**kwarg):
    u'''获取屏体列表,错误token'''
    url = getConf("constant","url")+'/mobile/screen/userScreen'    
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    strdict=json.loads(response.text)
#     return eval((response.text).replace("false","False").replace("true","True"))
    return strdict
def rq_monitorData(**kwarg):
    u'''获取单个屏体监控数据'''
    url = getConf("constant","url")+'/mobile/screen/monitorData'   
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    strdict=json.loads(response.text)
#     return eval((response.text).replace("false","False").replace("true","True"))
    return strdict
def rq_monitorDataE(**kwarg):
    u'''获取单个屏体监控数据,错误token '''
    url = getConf("constant","url")+'/mobile/screen/monitorData'   
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    strdict=json.loads(response.text)
#     return eval((response.text).replace("false","False").replace("true","True"))
    return strdict
def rq_cameraThumbnail(**kwarg):
    u'''获取屏体最新一张监控图片(缩略图)--多摄像机'''
    url = getConf("constant","url")+'/mobile/screen/cameraThumbnail'   
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))
def rq_cameraThumbnailE(**kwarg):
    u'''获取屏体最新一张监控图片(缩略图)--多摄像机,错误token '''
    url = getConf("constant","url")+'/mobile/screen/cameraThumbnail'   
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_cameraImage(**kwarg):
    u'''获取屏体最新一张监控图片(原始图)--多摄像机'''
    url = getConf("constant","url")+'/mobile/screen/cameraImage'    
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))
def rq_cameraImageE(**kwarg):
    u'''获取屏体最新一张监控图片(原始图)--多摄像机  ,错误token '''
    url = getConf("constant","url")+'/mobile/screen/cameraImage'    
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_Image(**kwarg):
    u'''获取屏体最新一张监控图片(原始图)'''
    url = getConf("constant","url")+'/mobile/screen/Image'   
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))
def rq_ImageE(**kwarg):
    u'''获取屏体最新一张监控图片(原始图)  ,错误token'''
    url = getConf("constant","url")+'/mobile/screen/Image'   
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))

def rq_thumbnail(**kwarg):
    u'''获取屏体最新一张监控图片(缩略图)'''
    url = getConf("constant","url")+'/mobile/screen/thumbnail'    
    headers = getHeaders()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))
def rq_thumbnailE(**kwarg):
    u'''获取屏体最新一张监控图片(缩略图) ,错误token'''
    url = getConf("constant","url")+'/mobile/screen/thumbnail'    
    headers = getHeadersE()
    response = requests.post(url=url,headers=headers,json=kwarg,verify = False)
    return eval((response.text).replace("false","False").replace("true","True"))





