import unittest

from parametrizedTestCase import ParametrizedTestCase
from test_A_terminal.test_terminal import Test_terminal
from test_B_main.test_clear import Test_clear
from test_B_main.test_getConstant import Test_getConstant
from test_B_main.test_getSession import Test_getSession
from test_C_single.ExtendDevice.getDeviceInfo import Test_getDeviceInfo
from test_C_single.MonitorPictureCurrent.test_current import Test_current
from test_C_single.MonitorPictureHistory.test_getHistoryListInfo import Test_getHistoryListInfo
from test_C_single.MonitorPictureHistory.test_getHistoryPhotoDateByScreenId import Test_getHistoryPhotoDateByScreenId
from test_C_single.MonitorPictureHistory.test_getHistoryPhotoTimeByCameraId import Test_getHistoryPhotoTimeByCameraId
from test_C_single.MonitorPictureSetting.test_cameraConfig import Test_cameraConfig
from test_C_single.MonitorPictureSetting.test_cameraSetting import Test_cameraSetting
from test_C_single.MonitorPictureSetting.test_cameras import Test_cameras
from test_C_single.MonitorPictureSetting.test_checkCameraSet import Test_checkCameraSet
from test_C_single.MonitorPictureSetting.test_clearMessage import Test_clearMessages
from test_C_single.MonitorPictureSetting.test_clearSetting import Test_clearSetting
from test_C_single.MonitorPictureSetting.test_detectionSetting import Test_detectionSetting
from test_C_single.MonitorPictureSetting.test_enabledCameras import Test_enabledCameras
from test_C_single.MonitorPictureSetting.test_nameSet import Test_nameSet
from test_C_single.MonitorPictureSetting.test_order import Test_order
from test_C_single.Monitoring.test_messages import Test_messages
from test_C_single.Monitoring.test_pictures import Test_pictures
from test_C_single.Monitoring.test_save_selects import Test_saveselects
from test_C_single.Monitoring.test_screens import Test_screens
from test_C_single.PersonalSetting.test_baseInfo import Test_baseInfo
from test_C_single.PersonalSetting.test_bindContactInfo import Test_bindContactInfo
from test_C_single.PersonalSetting.test_getUserInfo import Test_getUserInfo
from test_C_single.PersonalSetting.test_getVerifyCode import Test_getVerifyCode
from test_C_single.PersonalSetting.test_modifyPassword import Test_modifyPassword
from test_C_single.PersonalSetting.test_permissions import Test_permissions
from test_C_single.PersonalSetting.test_saveBaseInfo import Test_saveBaseInfo
from test_C_single.RealTimeStatus.test_emailList import Test_emailList
from test_C_single.RealTimeStatus.test_logList import Test_logList
from test_C_single.RealTimeStatus.test_realTime import Test_realTime
from test_C_single.RealTimeStatus.test_realTimeConfSet import Test_realTimeConfSet
from test_C_single.RealTimeStatus.test_realTimeConfig import Test_realTimeConfig
from test_C_single.Reports.test_customreport import Test_Customreport
from test_C_single.Reports.test_periodicInspectionReports import Test_PerodicInspectionReport
from test_C_single.ScreenInfo.test_getScreenInfoBySid import Test_getScreenInfoBySid
from test_C_single.ScreenInfo.test_saveScreenAlarmConf import Test_saveScreenAlarmConf
from test_C_single.ScreenInfo.test_saveScreenInfo import Test_saveScreenInfo
from test_C_single.ScreenList.test_getAllFilter import Test_getAllFilter
from test_C_single.ScreenList.test_getScreenList import Test_getScreenList
from test_C_single.SpotCheck.test_a_add import Test_add
from test_C_single.SpotCheck.test_b_getInfoById import Test_getInfoById
from test_C_single.SpotCheck.test_c_edit import Test_edit
from test_C_single.SpotCheck.test_d_list import Test_list
from test_C_single.SpotCheck.test_e_index import Test_index
from test_C_single.SpotCheck.test_f_getInfoBySid import Test_getInfoBySid
from test_C_single.SpotCheck.test_g_nameList import Test_nameList
from test_C_single.SpotCheck.test_h_set import Test_set
from test_C_single.SpotCheck.test_z_delete import Test_delete
# 2018-8-29
from test_D_app.CameraImage.test_CameraImage import Test_CameraImage
from test_D_app.CameraThumbnail.test_CameraThumbnail import Test_CameraThumbnail
from test_D_app.CheckPhone.test_CheckPhone import Test_CheckPhone
from test_D_app.CheckUserName.test_CheckUserName import Test_CheckUserName
from test_D_app.Detect.test_Detect import Test_Detect
from test_D_app.Image.test_Image import Test_Image
from test_D_app.Label.test_Label import Test_Label
from test_D_app.Login.test_Login import Test_Login
from test_D_app.MonitorData.test_MonitorData import Test_monitorData
from test_D_app.Send.test_Send import Test_send
from test_D_app.Thumbnail.test_Thumbnail import Test_thumbnail
from test_D_app.UserScreen.test_UserScreen import Test_userScreen
from test_E_wechat.AddImg.test_AddImg import Test_AddImg
from test_E_wechat.Detail.test_Detail import Test_Detail
from test_E_wechat.GetJsParam.test_GetJsParam import Test_GetJsParam
from test_E_wechat.feedback.test_feedback import Test_Feedback
from test_F_bug.test_bug1 import Test_bug
from test_F_bug.test_bug2 import Test_bug2
from test_F_bug.test_bug3 import Test_bug3
from test_G_websocket.test_websocket import Test_websocket


def addTestCase(request):

    # t = P_TestCase(param = requests)
    # discover1 = unittest.TestSuite()
    # discover1.addTest(ParametrizedTestCase.parametrize(Test_bug, param=request))
    # return discover1


    discover = unittest.TestSuite()

    '''getToken'''
    discover.addTest(ParametrizedTestCase.parametrize(Test_getSession,param = request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_clear,param = request))

    '''test_A_terminal'''

    discover.addTest(Test_terminal("test_aregister"))
    discover.addTest(Test_terminal("test_heartbeat"))
    discover.addTest(Test_terminal("test_getSreen"))

    discover.addTest(Test_terminal("test_bupdateConf"))
    discover.addTest(Test_terminal("test_cSpotCheck"))
    discover.addTest(Test_terminal("test_brightlog"))
    discover.addTest(Test_terminal("test_index"))
    # discover.addTest(Test_terminal("test_updateScreenStatus"))

    '''test_B_main'''
    discover.addTest(ParametrizedTestCase.parametrize(Test_getConstant, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_bug3, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_saveScreenAlarmConf, param=request))

    discover.addTest(Test_terminal("test_monitorData"))
    discover.addTest(Test_terminal("test_heartbeat"))
    discover.addTest(Test_terminal("test_monitorData"))
    discover.addTest(Test_terminal("test_heartbeat"))
    discover.addTest(Test_terminal("test_monitorData"))
    discover.addTest(Test_terminal("test_heartbeat"))
    discover.addTest(Test_terminal("test_monitorData"))
    discover.addTest(Test_terminal("test_heartbeat"))
    discover.addTest(Test_terminal("test_monitorData"))
    discover.addTest(Test_terminal("test_heartbeat"))
    discover.addTest(Test_terminal("test_monitorData"))



    '''test_C_single'''

    # # reports
    discover.addTest(ParametrizedTestCase.parametrize(Test_PerodicInspectionReport, param=request))

    discover.addTest(ParametrizedTestCase.parametrize(Test_Customreport, param=request))

    # extendDevice
    discover.addTest(ParametrizedTestCase.parametrize(Test_getDeviceInfo,param=request))

    # # monitoring
    discover.addTest(ParametrizedTestCase.parametrize(Test_messages, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_pictures, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_saveselects, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_screens, param=request))

    # # monitorPictureCurrent
    discover.addTest(ParametrizedTestCase.parametrize(Test_current, param=request))


    # # monitorPictureCurrent
    discover.addTest(ParametrizedTestCase.parametrize(Test_getHistoryListInfo, param=request))

    discover.addTest(ParametrizedTestCase.parametrize(Test_getHistoryPhotoDateByScreenId, param=request))

    discover.addTest(ParametrizedTestCase.parametrize(Test_getHistoryPhotoTimeByCameraId, param=request))
    #
    # # monitorPictureSetting
    discover.addTest(ParametrizedTestCase.parametrize(Test_cameraConfig, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_cameras, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_cameraSetting, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_checkCameraSet, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_clearMessages, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_clearSetting, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_detectionSetting, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_enabledCameras, param=request))
    # discover.addTest(ParametrizedTestCase.parametrize(Test_enableSet, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_nameSet, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_order, param=request))
    #
    #
    # # personalSetting
    discover.addTest(ParametrizedTestCase.parametrize(Test_baseInfo, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_bindContactInfo, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_getUserInfo, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_getVerifyCode, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_modifyPassword, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_permissions, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_saveBaseInfo, param=request))
    #
    #
    # # realTimeStatus
    discover.addTest(ParametrizedTestCase.parametrize(Test_emailList, param=request))

    discover.addTest(ParametrizedTestCase.parametrize(Test_realTime, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_realTimeConfig, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_realTimeConfSet, param=request))


    #

    #
    # # sreenInfo
    discover.addTest(ParametrizedTestCase.parametrize(Test_getScreenInfoBySid, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_saveScreenInfo, param=request))
    #
    #
    # # screenList
    discover.addTest(ParametrizedTestCase.parametrize(Test_getAllFilter, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_getScreenList, param=request))
    #
    #
    # # spotCheck
    discover.addTest(ParametrizedTestCase.parametrize(Test_add, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_getInfoById, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_edit, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_list, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_index, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_getInfoBySid, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_nameList, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_set, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_delete, param=request))



    #others
    discover.addTest(ParametrizedTestCase.parametrize(Test_order, param=request))
    '''test_F_bug'''
    discover.addTest(ParametrizedTestCase.parametrize(Test_bug, param=request))

    '''test_G_websocket'''
    discover.addTest(Test_websocket("test_a_register"))
    discover.addTest(Test_websocket("test_b_bind"))
    discover.addTest(Test_websocket("test_c_updateConf"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_d_minitorData"))
    discover.addTest(Test_websocket("test_e_index"))
    discover.addTest(Test_websocket("test_f_brightlog"))
    discover.addTest(Test_websocket("test_g_SpotCheck"))

    #2018-8-29
    '''test_D_app'''
    discover.addTest(Test_Login("test_a"))
    discover.addTest(Test_Login("test_b"))
    discover.addTest(Test_Login("test_c"))

    discover.addTest(Test_CameraImage("test_a"))

    discover.addTest(Test_CameraThumbnail("test_a"))



    discover.addTest(Test_CheckPhone("test_a"))
    # discover.addTest(Test_CheckPhone("test_b"))
    # discover.addTest(Test_CheckPhone("test_c"))

    discover.addTest(Test_CheckUserName("test_a"))
    discover.addTest(Test_CheckUserName("test_b"))

    discover.addTest(Test_Detect("test_a"))
    discover.addTest(Test_Detect("test_b"))
    discover.addTest(Test_Detect("test_c"))
    discover.addTest(Test_Detect("test_d"))

    discover.addTest(Test_Image("test_a"))
    discover.addTest(Test_Image("test_b"))
    discover.addTest(Test_Image("test_c"))

    discover.addTest(Test_Label("test_a"))
    discover.addTest(Test_Label("test_b"))
    discover.addTest(Test_Label("test_c"))

    discover.addTest(Test_monitorData("test_a"))
    discover.addTest(Test_monitorData("test_b"))
    discover.addTest(Test_monitorData("test_c"))
    #     discover.addTest(Test_monitorData("test_d"))
    discover.addTest(Test_monitorData("test_e"))

    #     discover.addTest(Test_register("test_a"))
    #     discover.addTest(Test_register("test_b"))
    #     discover.addTest(Test_register("test_c"))

    discover.addTest(Test_send("test_a"))
    discover.addTest(Test_send("test_b"))
    discover.addTest(Test_send("test_c"))

    discover.addTest(Test_thumbnail("test_a"))
    discover.addTest(Test_thumbnail("test_b"))

    discover.addTest(Test_userScreen("test_a"))
    discover.addTest(Test_userScreen("test_b"))
    # discover.addTest(Test_userScreen("test_c"))

    '''test_E_wechat'''
    discover.addTest(Test_AddImg("test_a"))

    discover.addTest(Test_Detail("test_a"))

    discover.addTest(Test_Feedback("test_a"))

    discover.addTest(Test_GetJsParam("test_a"))

    return discover


def addTestCase1(request):
    discover = unittest.TestSuite()
    discover.addTest(ParametrizedTestCase.parametrize(Test_bug2, param=request))
    discover.addTest(ParametrizedTestCase.parametrize(Test_logList, param=request))
    return discover






