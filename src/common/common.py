#coding=utf-8


import requests
from flask import json

from tools.tools import  getHeaders, getConf


# def getStorCookie():
#     url = getConf('constant', 'url')+"/login/loginCheck"
#     headers = {}
#     headers["Origin"] = "http://t-docker.novaicare.com"
#     headers["Host"] = getConf("constant","url").split(r"//")[1]
#     headers["X-Requested-With"] = "XMLHttpRequest"
#     
#     data = "username=jiqun&password=123456"
#     
#     response = requests.post(url,headers=headers,data=data)
#     print response.text
#     url = getConf("constant","url")+"/login/index/redirect/%252F.html"
#     headers = {}
#     headers["Cache-Control"] = "no-cache"
#     headers["Host"] = getConf("constant","url").split(r"//")[1]
#     headers["Pragma"] = "no-cache"
#     response = requests.get(url,headers=headers)
#     Cookies = dict(response.headers)["Set-Cookie"].split(";")[0]
#     print Cookies
#     print response.text
#     setConf("data","Cookie",Cookies)
def asseetprint(name,actual,expect):
    if expect in actual:
        print name+":"+expect+","+actual
        return True
    else:
        print name+":"+expect+","+actual+" === Request interface failed"
        return False
    
# def rq_0():
#     u'''登陆后获取屏体的信息'''
#     url = getConf("constant","url")+"/Screen/getListForJson/type/AJAX/status/0"
#     headers = getHeaders()
#     response = requests.get(url=url,headers=headers)
#     return json.loads(response.text)

'''     现场画面设置              '''

def rq_cameras(r,**kwarg):
    u'''获取屏体摄像机列表 '''
    url = getConf("constant", "url")+"/new/backend/camera/cameras"
    headers = getHeaders()
    response = r.request(method='get', url=url,headers=headers,params=kwarg)
    print "response::" + response.text
    response.encoding = 'utf-8'
    return json.loads(response.text)

def rq_cameraConfig(r,**kwarg):
    u'''获取屏体摄像机配置'''
    url = getConf("constant", "url")+"/new/backend/camera/cameraConfig"
    headers = getHeaders()
    response = r.request(method='get', url=url,headers=headers,params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_cameraSetting(r,**kwarg):
    u'''保存屏体摄像机配置'''
    url = getConf("constant", "url")+"/new/backend/camera/cameraSetting"
    headers = getHeaders()
    response = r.request(method='post', url=url,headers=headers,params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_checkCameraSet(r,**kwarg):
    u'''检测摄像机配置'''
    url = getConf("constant", "url")+"/new/backend/camera/checkCameraSet"
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_clearSetting(r,**kwarg):
    u'''获取摄像机图片清理设置'''
    url = getConf("constant", "url")+"/new/backend/camera/clearSetting"
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_detectionSetting(r,**kwarg):
    u'''获取屏体故障感知设置'''
    url = getConf("constant", "url")+"/new/backend/camera/detectionSetting"
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_enableSet(r,**kwarg):
    u'''修改摄像机开启状态'''
    url = getConf("constant", "url")+"/new/backend/camera/enableSet"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_nameSet(r,**kwarg):
    u'''修改摄像机名称'''
    url = getConf("constant", "url")+"/new/backend/camera/nameSet"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)


def rq_order(r,**kwarg):
    u'''修改摄像机排序'''
    url = getConf("constant", "url")+"/new/backend/camera/order"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_enabledCameras(r,**kwarg):
    u'''获取屏体已开启的摄像机列表'''
    url = getConf("constant", "url")+"/new/backend/camera/enabledCameras"
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_clearmessages(r,**kwarg):
    u'''清空监控画面屏体故障、离线消息列表'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/clear-messages"   

    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
    
'''     现场画面最新          '''
    
def rq_current(r,**kwarg):
    u'''获取屏体当前画面列表'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/current"   
    headers = getHeaders()
    response = r.request(method='post', url=url,headers=headers,json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)


'''   现场画面历史图片          '''
    
def rq_getHistoryPhotoDateByScreenId(r,**kwarg):
    u'''获取历史图片目录列表'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/getHistoryPhotoDateByScreenId"  
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_getHistoryListInfo(r,**kwarg):
    url = getConf("constant", "url")+"/new/backend/monitor-picture/getHistoryListInfo"
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
    
def rq_getHistoryPhotoTimeByCameraId(r,**kwarg):
    u'''获取历史图片目录内图片列表'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/getHistoryPhotoTimeByCameraId"  
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
    
'''      画面监控              '''
    
    
def rq_messages(r,**kwarg):
    u'''获取监控画面屏体故障、离线消息列表'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/messages"  
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_pictures(r,**kwarg):
    u'''获取屏体摄像机最新图片列表'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/pictures"  
    headers = getHeaders()
#     params = loadParams(data,["sid","grid"])
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_screens(r,**kwarg):
    u'''监控画面获取所有屏体信息'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/screens"  
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_save_selects(r,**kwarg):
    u'''保存监控画面已选择屏体'''
    url = getConf("constant", "url")+"/new/backend/monitor-picture/save-selects"  
    headers = getHeaders()
#     params = loadParams(data,["selects"])
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
    
    
'''   屏体基本信息         '''
    
def rq_getScreenInfoBySid(r,**kwarg):
    u'''获取屏体基本想信息'''
    url = getConf("constant", "url")+"/new/backend/screen/getScreenInfoBySid"  
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
    
def rq_saveScreenAlarmConf(r,**kwarg):
    url = getConf("constant", "url")+"/new/backend/screen/saveScreenAlarmConf"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_saveScreenInfo(r,**kwarg):
    url = getConf("constant", "url")+"/new/backend/screen/saveScreenInfo"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    

'''   个人设置    '''

       
def rq_baseInfo(r,**kwarg):
    u'''获取用户基本信息'''
    url = getConf("constant", "url")+"/new/backend/user/baseInfo"  
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_getVerifyCode(r,**kwarg):
    url = getConf("constant", "url")+"/new/backend/user/getVerifyCode"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_bindContactInfo(r,**kwarg):
    url = getConf("constant", "url")+"/new/backend/user/bindContactInfo"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_modifyPassword(r,**kwarg):
    url = getConf("constant", "url")+"/new/backend/user/modifyPassword"
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_getUserInfo(r,**kwarg):
    u'''获取用户详细信息'''
    url = getConf("constant", "url")+"/new/backend/user/getUserInfo"  
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_permissions(r,**kwarg):
    u'''获取用户权限信息'''
    url = getConf("constant", "url")+"/new/backend/user/permissions"  
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    

def rq_saveBaseInfo(r,**kwarg):
    u'''保存基本信息'''
    url = getConf("constant", "url")+"/new/backend/user/saveBaseInfo"  
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    
def rq_setLanguage(r,**kwarg):
    u'''保存基本信息'''
    url = getConf("constant", "url")+"/public/setLanguage"  
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    

'''     扩展设备        '''    
    
def rq_getDeviceInfo(r,**kwarg):
    url = getConf("constant", "url")+"/new/backend/screen/getDeviceInfo"
    headers = getHeaders()
    response = r.post(url=url,headers=headers,json = kwarg)
    print "response::" + response.text
    return json.loads(response.text)


'''      点检                   '''
def rq_getInfoBySid(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/setSpotCheck/getInfoBySid'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_index(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/setSpotCheck/index'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_set(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/setSpotCheck/set'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_setBatch(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/setSpotCheck/setBatch'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

'''       点检模板              '''
def rq_nameList(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/checkTemp/nameList'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_edit(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/checkTemp/edit'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_list(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/checkTemp/list'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_delete(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/checkTemp/delete'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_getInfoById(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/checkTemp/getInfoById'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_add(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/checkTemp/add'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)



'''      巡检报告                '''
def rq_detail(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/report/detail'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_history(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/report/history'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_screenDetail(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/report/setting/screen/detail'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_settingDetail(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/report/setting/detail'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_screenEdit(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/report/setting/screen/edit'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::"+ response.text
    return json.loads(response.text)

def rq_settingEdit(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/report/setting/edit'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)


''' 实时状态 '''

def rq_realTime(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/realTime'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_logList(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/logList'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_emailList(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/emailList'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_realTimeConfig(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/realTimeConfig'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_realTimeConfSet(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/realTimeConfSet'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_exportLogList(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/exportLogList'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)



# 
# file = rq_exportLogList(sid=getConf('data', 'sid'),lang='zh_cn',token=(getConf('constant', 'authorization')).split(" ")[-1])
# # print  base64.b64decode(file.encode('utf-8'))
# print  file.encode('utf-8')

''' 显示屏列表 '''

def rq_getScreenList(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/getScreenList'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_getAllFilter(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/getAllFilter'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_deleteScreen(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/screen/deleteScreen'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

# get secreted sid
def rq_setEncrypt(r,**kwarg):
    url = getConf("constant", "url")+'/new/backend/system/setEncrypt'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)["data"]

'''others'''
def rq_getShowNotice(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/notice/getShowNotice'
    headers = getHeaders()
    response = r.request(method='get', url=url, headers=headers, params=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

'''test_bug'''
def rq_saveClientReportParamaterSet(r,**kwarg):
    url = getConf("constant", "url") + '/CustomizedReport/saveClientReportParamaterSet'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, data=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_saveReportScreenSet(r,**kwarg):
    url = getConf("constant", "url") + '/CustomizedReport/saveReportScreenSet'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, data=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_reportSetList(r,**kwarg):
    url = getConf("constant", "url") + '/CustomizedReport/reportSetList'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, data=kwarg)
    print "response::" + response.text
    return json.loads(response.text)

def rq_deleteSetup(r,**kwarg):
    url = getConf("constant", "url") + '/CustomizedReport/DeleteSetup'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)



u'''      客户定制报告 新增客户定制报告配置           '''
def rq_customreportsave(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/custom-report/setup/save'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
u'''      客户定制报告   关联屏体         '''
def rq_customreportedit(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/custom-report/setup/relation/edit'
    headers = getHeaders()
    response = r.request(method='post', url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
    u'''      删除客户定制报告配置        '''
def rq_customreportdelete(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/custom-report/setup/delete'
    headers = getHeaders()
    response = r.request(method='post',url=url, headers=headers, json=kwarg)
    print "response::" + response.text
    return json.loads(response.text)
u'''      客户定制报告 获取客户定制报告配置           '''
def rq_getcustomreport(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/custom-report/setup?currentPage=1&keyword=&orderName=cr_Name&orderType=asc&pageSize=10'
    headers = getHeaders()
    response = r.request(method='get',url=url, headers=headers)
    print "response::" + response.text
    return json.loads(response.text)

u'''      保存企业信息配置           '''
def rq_saveSystemConfig(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/enterprise/saveSystemConfig'
    headers = getHeaders()
    response = r.request(method='post',url=url,headers=headers,json=kwarg,verify = False)
    
    return json.loads(response.text)

u'''      获取企业信息配置           '''
def rq_getEnterpriseInfo(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/enterprise/getEnterpriseInfo'
    headers = getHeaders()
    response = r.request(method='get',url=url,headers=headers,verify = False)
    
    return json.loads(response.text)


u'''      保存企业信息配置           '''
def rq_saveSystemConfig(r,**kwarg):
    url = getConf("constant", "url") + '/new/backend/enterprise/saveSystemConfig'
    headers = getHeaders()
    response = r.request(method='post',url=url,headers=headers,json=kwarg,verify = False)
    
    return json.loads(response.text)



















    
    
    
    
    
    
    

 
    