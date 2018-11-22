#coding=utf-8
import ConfigParser
import email
from email.mime.image import MIMEImage
import json
import os
import random


def readFileAsDict(relative_path='json_case/terminal/monitorData'):
    if os.path.isfile("./" + relative_path):
        file = os.path.abspath("./" + relative_path)
    elif os.path.isfile("../" + relative_path):
        file = os.path.abspath("../" + relative_path)
    elif os.path.isfile("../../" + relative_path):
        file = os.path.abspath("../../" + relative_path)
    elif os.path.isfile("../../../" + relative_path):
        file = os.path.abspath("../../../" + relative_path)
    else:
        raise Exception("give the wrong relative_path")   
    f = open(file) 
    str = f.read()
    f.close()
    result = eval(str)
    return result
    
            
             
def sendMail():
    import smtplib
    from email.mime.text import MIMEText
     
    my_sender = 'novatest@126.com'    # 发件人邮箱账号
    my_pass = 'nova123456'    # 发件人邮箱密码
    # my_user = 'novatest@126.com'   # 收件人邮箱账号
    my_user = getConf('data','email')   # 收件人邮箱账号

    msg = email.MIMEMultipart.MIMEMultipart()
    
    msg1=MIMEText(open(new_report()).read(),'html','utf-8')
    
    
    #添加二进制附件  
      
    ctype = 'application/octet-stream'  
    maintype, subtype = ctype.split('/', 1)  
    att1 = MIMEImage(open(new_report()).read(), _subtype = subtype)
    fileName = new_report().split("\\")[-1]  
    att1.add_header('Content-Disposition', 'attachment', filename = fileName)  
    msg.attach(att1)  
    
    
    
    msg.attach(msg1)
    msg['From']=my_sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=my_user            # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']=u"care interface test"                # 邮件的主题，也可以说是标题

    server=smtplib.SMTP("smtp.126.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
#     server.set_debuglevel(1)
    server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,my_user.split(','),msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit() # 关闭连接
    print 'send mail success'

        
def new_report():
    result_dir = './report'
    result_dir = os.path.abspath(result_dir)
    file = os.path.join(result_dir,getConf('data','fileName'))
    return file  



def store(data):
    u'''
        data: 需要向配置文件中存储的数据，一定要为字典类型
    '''
    data = dict( load(), **data ) #将两个字典合并
    if os.path.isfile("./config.json"):
        with open('./config.json','w') as json_file:
            json_file.write(json.dumps(data))
    elif os.path.isfile("../config.json"):
        with open('../config.json','w') as json_file:
            json_file.write(json.dumps(data))
    elif os.path.isfile('../../config.json'):
        with open('../../config.json','w') as json_file:
            json_file.write(json.dumps(data))
    else:
        raise Exception("wrong path of config.json")  


def load():
    if os.path.isfile("./config.json"):
        with open('./config.json') as json_file:
            data = json.load(json_file)
    elif os.path.isfile("../config.json"):
        with open('../config.json') as json_file:
            data = json.load(json_file)
    elif os.path.isfile('../../config.json'):
        with open('../../config.json') as json_file:
            data = json.load(json_file)
    else:
        raise Exception("wrong path of config.json")  
    return data  

def loadParams(data,list):
    u'''
        data: 读取的配置文件信息
        list: 请求参数的列表
                      返回一个字典类型的params
    '''
    params = {}
    for li in list:
        params[li] = data[li]
    return params

def changeParams(params,info,list):
    u'''
        params: 在读取的配置文件中读到的参数
        info: 从json_case中读到的请求信息
        list: 请求参数的列表
                      无返回值
        
        ps:当从json_case中读到参数时将其覆盖之前从配置文件中读到的
                                当从json_case中读到的参数值为“-”时，表示请求时不带此参数
    '''
    tmp = params.copy()
    if info.has_key("params"):
        for li in list:        
            if info["params"].has_key(li):
                tmp[li] = info["params"][li]
                if info["params"][li] == "-":
                    tmp.pop(li)
    return tmp    
def changeHeaders(info,headers):
    u'''
        info: 从json_case读取到的某一条数据
        headers: 在配置文件中读取到的请求头
                        返回字典类型的headers(是结合json_case后得到的，区别于loadHeaders)
    '''
    tmp = headers.copy()
    if info.has_key("headers"):
    
        if info["headers"].has_key("Authorization"):
            tmp["Authorization"] = info["headers"]["Authorization"]
            if info["headers"]["Authorization"] == "-":
                tmp.pop("Authorization")
            
        if info["headers"].has_key("Cookies"):
            tmp["Cookies"] = info["headers"]["Cookies"]
            if info["headers"]["Cookies"] == "-":
                tmp.pop("Cookies")
    return tmp

def getHeaders():
    u'''获取请求头'''
    headers = {}
    headers["Authorization"] = getConf("constant", "authorization")
    headers["Cookie"] = getConf("data", "cookie")
    headers["token"] = getConf("data", "token")
    return headers

def verify_rp(info,response):
    u'''
        info: 从json_case读取到的某一条数据
        response: 请求后的返回值
                        打印执行结果
                        返回flag，执行成功返回True,执行失败返回Flase
    '''
    flag = True
    print response.text
    response = eval((response.text).replace("null","None").replace("false","False").replace("true","True"))
    if response["status"]==info["expect"]["status"]:
        if info["expect"].has_key("data"): 
            if response["data"]==info["expect"]["data"]:
                print u"%s %s 执行成功,期望值为%s,实际值为%s"%(info["number"],info["describe"].decode('utf8'),info["expect"],response)
            else:
                print u"%s %s 执行失败,期望值为%s,实际值为%s"%(info["number"],info["describe"].decode('utf8'),info["expect"],response)
                flag = False
        else:
            print u"%s %s 执行成功,期望值为%s,实际值为%s"%(info["number"],info["describe"].decode('utf8'),info["expect"],response)
    else :
        print u"%s %s 执行失败,期望值为%s,实际值为%s"%(info["number"],info["describe"].decode('utf8'),info["expect"],response)
        flag = False
    
    return flag

def myAlign(string, length=0):  
    if length == 0:  
        return string  
    slen = len(string)  
    re = string  
    if isinstance(string, str):  
        placeholder = ' '  
    else:  
        placeholder = u'　'  
    while slen < length:  
        re += placeholder  
        slen += 1  
    return re  


def getConf(section,option):
    cp = ConfigParser.ConfigParser()
    if os.path.isfile("./interface.conf"):
        cp.read("./interface.conf")
    elif os.path.isfile("../interface.conf"):
        cp.read("../interface.conf")
    elif os.path.isfile("../../interface.conf"):
        cp.read("../../interface.conf")   
    else:
        raise Exception("wrong path of interface.conf")
    
    return cp.get(section, option)

def setConf(section, option, value):
    cp = ConfigParser.ConfigParser()
    if os.path.isfile("./interface.conf"):
        cp.read("./interface.conf")
        cp.set(section, option, value)
        cp.write(open("./interface.conf", "w"))
    elif os.path.isfile("../interface.conf"):
        cp.read("../interface.conf")
        cp.set(section, option, value)
        cp.write(open("../interface.conf", "w"))
    elif os.path.isfile("../../interface.conf"):
        cp.read("../../interface.conf") 
        cp.set(section, option, value)
        cp.write(open("../../interface.conf", "w"))  
    else:
        raise Exception("wrong path of interface.conf")
    
    
def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999,100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)

#2018-8-29
def getHeadersE():
    u'''获取错误请求头,错误token'''
    headers = {}
    headers["Authorization"] = getConf("constant", "Authorization")
    headers["Cookie"] = getConf("data", "Cookie")
    headers["token"] = getConf("data", "tokenE")
    return headers



if __name__ == "__main__" :
    setConf("data","sid","234")    
    
    
    
