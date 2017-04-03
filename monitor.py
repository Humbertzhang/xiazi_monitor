#coding:utf-8
from __future__ import absolute_import
import requests
import base64
import json
import redis
from requests.auth import HTTPBasicAuth
from celery import Celery
from flask import Flask,jsonify
from werkzeug.contrib.cache import SimpleCache
from celery.schedules import crontab
from datetime import timedelta
from os import sys,path
from make_celery import make_celery
from flask_script import Manager 

#
TOTAL = 144

#每次检查间隔时间
TIME_EVERY_CHECK=10

#set i
i = 0

#redis链接池
pool01 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
pool02 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2)
pool03 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=3)
pool04 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=4)
pool05 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=5)
pool06 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=6)
pool07 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=7)
pool08 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=8)
pool09 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=9)
pool10 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=10)
pool11 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=11)
pool12 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=12)
pool13 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=13)
pool14 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=14)
pool15 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=15)
pool16 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=16)
pool17 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=17)
pool18 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=18)
pool19 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=19)
pool21 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=21)
pool22 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=22)
pool23 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=23)
pool24 = redis.ConnectionPool(host='127.0.0.1', port=6379, db=24)
r01 = redis.StrictRedis(connection_pool=pool01)
r02 = redis.StrictRedis(connection_pool=pool02)
r03 = redis.StrictRedis(connection_pool=pool03)
r04 = redis.StrictRedis(connection_pool=pool04)
r05 = redis.StrictRedis(connection_pool=pool05)
r06 = redis.StrictRedis(connection_pool=pool06)
r07 = redis.StrictRedis(connection_pool=pool07)
r08 = redis.StrictRedis(connection_pool=pool08)
r09 = redis.StrictRedis(connection_pool=pool09)
r10 = redis.StrictRedis(connection_pool=pool10)
r11 = redis.StrictRedis(connection_pool=pool11)
r12 = redis.StrictRedis(connection_pool=pool12)
r13 = redis.StrictRedis(connection_pool=pool13)
r14 = redis.StrictRedis(connection_pool=pool14)
r15 = redis.StrictRedis(connection_pool=pool15)
r16 = redis.StrictRedis(connection_pool=pool16)
r17 = redis.StrictRedis(connection_pool=pool17)
r18 = redis.StrictRedis(connection_pool=pool18)
r19 = redis.StrictRedis(connection_pool=pool19)
r21 = redis.StrictRedis(connection_pool=pool21)
r22 = redis.StrictRedis(connection_pool=pool22)
r23 = redis.StrictRedis(connection_pool=pool23)
r24 = redis.StrictRedis(connection_pool=pool24)

#信息门户头部信息
usrPass = "2016210942:130395"
b64Val = base64.b64encode(usrPass)

#图书馆头部信息
Passlib ="2016210942:123456"
b64Vallib = base64.b64encode(Passlib)

#管理员头部信息
adminPass = "muxistudio@qq.com:<!--muxi-->"
b64admin = base64.b64encode(adminPass)

#初始化APP
app = Flask(__name__)

#初始化Cache
cache23 = SimpleCache()
cache24 = SimpleCache()
#URLS
url01 = "https://ccnubox.muxixyz.com/api/info/login/"
url02 = "https://ccnubox.muxixyz.com/api/lib/login/"
url03 = "https://ccnubox.muxixyz.com/api/lib/search/?keyword=计算机&page=1"
url04 = "https://ccnubox.muxixyz.com/api/lib/?id=0000475103"
url05 = "https://ccnubox.muxixyz.com/api/lib/me/"
url06 = "https://ccnubox.muxixyz.com/api/table/"
url07 = "https://ccnubox.muxixyz.com/api/table/"
url08 = "https://ccnubox.muxixyz.com/api/ios/table/"
url09 = "https://ccnubox.muxixyz.com/api/table/5/"
url10 = "https://ccnubox.muxixyz.com/api/ios/table/5/"
url11 = "https://ccnubox.muxixyz.com/api/ele/"
url12 = "https://ccnubox.muxixyz.com/api/ele/"
url13 = "https://grade.muxixyz.com/api/grade/search/?xnm=2016&xqm=3/"
url14 = "https://ccnubox.muxixyz.com/api/apartment/"
url15 = "https://ccnubox.muxixyz.com/api/site/"
url16 = "https://ccnubox.muxixyz.com/api/info/"
url17 = "https://ccnubox.muxixyz.com/api/banner/"
url18 = "https://ccnubox.muxixyz.com/api/ios/banner/"
url19 = "https://ccnubox.muxixyz.com/api/calendar/"
url20 = "https://ccnubox.muxixyz.com/api/ios/calendar/"
url21 = "https://ccnubox.muxixyz.com/api/start/"
url22 = "https://ccnubox.muxixyz.com/api/feedback/"
url23 = "https://ccnubox.muxixyz.com/api/ios/config/"
url24 = "https://ccnubox.muxixyz.com/api/product/"

#以便返回汉字
app.config['JSON_AS_ASCII'] = False

#配置
app.config.update(
    
    CELERY_BROKER_URL='redis://127.0.0.1:6379',
    CELERY_RESULT_BACKEND='redis://127.0.0.1:6379/0',
    #Timezone
    CELERY_TIMEZONE = 'Asia/Shanghai',

    CELERYBEAT_SCHEDULE = {
        'login_xinximenhu':{
            'task': 'login_xinximenhu',
            'schedule': timedelta(seconds = TIME_EVERY_CHECK),
        },
        'login_library':{
            'task':'login_lib',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'find_books':{
            'task':'find_book',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'booksinfo':{
            'task':'book_info',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'mylib':{
            'task':'my_lib',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'inqu_table':{
            'task':'inqu_table',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'add_classes':{
            'task':'add_class',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'add_classes_ios':{
            'task':'add_class_ios',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'delete_class':{
            'task':'delete_class',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
	    'edit_table':{
            'task':'edit_table',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'ele_air':{
            'task':'ele_air',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'ele_light':{
            'task':'ele_light',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'grade_total':{
            'task':'grade_total',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'grade_detail':{
            'task':'grade_detail',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'apartment':{
            'task':'apartment',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'site':{
            'task':'site',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'info':{
            'task':'info',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'banner':{
            'task':'banner',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'banner_ios':{
            'task':'banner_ios',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'calendar':{
            'task':'calendar',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'start':{
            'task':'start',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'product':{
            'task':'product',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'feedback':{
            'task':'feedback',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
        'config_ios':{
            'task':'config_ios',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
        },
       'controli':{
            'task':'controli',
            'schedule':timedelta(seconds = TIME_EVERY_CHECK),
       },
    })

#初始化Celery
celery = make_celery(app)

#tasks

#信息门户登录
@celery.task(name='login_xinximenhu')
def login_xinximenhu():
    resp01 = requests.get("https://ccnubox.muxixyz.com/api/info/login/",\
                            headers = {"Authorization": "Basic %s" %b64Val})
    statu01 = resp01.status_code
    r01.set(i,statu01)
 
#登录图书馆 
@celery.task(name='login_lib')
def login_lib():
    resp02= requests.get("https://ccnubox.muxixyz.com/api/lib/login/",\
                            headers = {"Authorization": "Basic %s" %b64Vallib})
    statu02 = resp02.status_code
    r02.set(i,statu02)

#查询图书
@celery.task(name='find_book')
def find_book():
    resp03 = requests.get("https://ccnubox.muxixyz.com/api/lib/search/?keyword=计算机&page=1")
    statu03 = resp03.status_code
    r03.set(i,statu03)

#图书详情
@celery.task(name='book_info')
def book_info():
    resp04 = requests.get("https://ccnubox.muxixyz.com/api/lib/?id=0000475103")
    statu04 = resp04.status_code
    r04.set(i,statu04)

#我的图书馆
@celery.task(name='my_lib')
def my_lib():
    resp05 = requests.get("https://ccnubox.muxixyz.com/api/lib/me/",\
                            headers = {"Authorization": "Basic %s" % b64Vallib})
    statu05 = resp05.status_code
    r05.set(i,statu05)

#查询课表
@celery.task(name='inqu_table')
def inqu_table():
    resp06=requests.get("https://ccnubox.muxixyz.com/api/table/",\
                            headers = {"Authorization":"Basic %s" %b64Val})
    statu06 = resp06.status_code
    r06.set(i,statu06)


#添加课程
@celery.task(name='add_class')
def add_class():
    post_data={
            "id":"5",
            "course":"test",
            "teacher":"test",
            "weeks":"1,2,3,4",
            "day":"星期1",
            "start":"1",
            "during":"1",
            "place":"9-11",
            "remind":False
    }
    resp07=requests.post("https://ccnubox.muxixyz.com/api/table/",\
                            params = post_data,\
                            headers = {"Authorization":"Basic %s" %b64Val} )
    statu07 = resp07.status_code
    r07.set(i,statu07)

#添加课程 For IOS
@celery.task(name='add_class_ios')
def add_class_ios():
    post_data={
            "course":"test",
            "teacher":"test",
            "weeks":"1,2,3,4",
            "day":"星期1",
            "start":"3",
            "during":"2",
            "place":"9-21",
            "remind":False
        }
    resp08=requests.post("https://ccnubox.muxixyz.com/api/ios/table/",\
                            params = post_data,\
                            headers = {"Authorization":"Basic %s" %b64Val} )
    statu08 = resp08.status_code
    r08.set(i,statu08)

#删除课程 ID 为课程ID
@celery.task(name='delete_class')
def delete_class():
    resp09 = requests.delete("https://ccnubox.muxixyz.com/api/table/5/",\
                                        headers = {"Authorization":"Basic %s" %b64Val} )
    statu09=resp09.status_code
    r09.set(i,statu09)

#编辑课表
@celery.task(name='edit_table')
def edit_table():
    post_data={
            "course":"爱情心理学",
            "teacher":"余海军",
            "weeks":"1,2,3,4",
            "day":"6",
            "start":"6",
            "during":"2",
            "place":"9-11",
            "remind":False
    }    
    resp10 = requests.put( "https://ccnubox.muxixyz.com/api/table/5/",\
                                        params = post_data ,\
                                        headers = {"Authorization":"Basic %s" %b64Val} )

    statu10=resp10.status_code
    r10.set(i,statu10)

#空调电费查询
@celery.task(name='ele_air')
def ele_air():
    post_data = {
        "dor":"东1-101",
        "type": "air"
    }
    resp11 = requests.post("https://ccnubox.muxixyz.com/api/ele/",\
                                params = post_data)
    statu11=resp11.status_code
    r11.set(i,statu11)    

#照明电费查询
@celery.task(name='ele_light')
def ele_light():
    post_data = {
        "dor":"东1-101",
        "type": "light"
        }
    resp12 = requests.post(   "https://ccnubox.muxixyz.com/api/ele/",\
                                        params = post_data  )
    statu12=resp12.status_code
    r12.set(i,statu12)

#成绩查询
@celery.task(name='grade_total')
def grade_total():
    resp13 = requests.get("https://grade.muxixyz.com/api/grade/search/?xnm=2016&xqm=3/",\
                            headers = {"Authorization":"Basic %s" %b64Val} )
    
    statu13=resp13.status_code
    r13.set(i,statu13)


#平时成绩查询
@celery.task(name='grade_detail')
def grade_detail():
    pass;

#部门信息
@celery.task(name='apartment')
def apartment():
    resp14 = requests.get("https://ccnubox.muxixyz.com/api/apartment/")
    statu14 = resp14.status_code
    r14.set(i,statu14)

#常用网站
@celery.task(name='site')
def site():
    resp15 = requests.get("https://ccnubox.muxixyz.com/api/site/")
    statu15 = resp15.status_code
    r15.set(i,statu15)

#通知公告
@celery.task(name='info')
def info():
    resp16 = requests.get("https://ccnubox.muxixyz.com/api/info/")
    statu16 = resp16.status_code
    r16.set(i,statu16)

#Banner获取
@celery.task(name='banner')
def banner():
    resp17 = requests.get("https://ccnubox.muxixyz.com/api/banner/")
    statu17 = resp17.status_code
    r17.set(i,statu17)

#Banner获取IOS
@celery.task(name='banner_ios')
def banner_ios():
    resp18 = requests.get("https://ccnubox.muxixyz.com/api/ios/banner/") 
    statu18 = resp18.status_code
    r18.set(i,statu18)

#校历
@celery.task(name='calendar')
def calendar():
    resp19 = requests.get("https://ccnubox.muxixyz.com/api/calendar/")
    statu19 = resp19.status_code
    r19.set(i,statu19)

#校历IOS
#@celery.task(name='calendar_ios')
#def calendar_ios():
#    resp20 = requests.get("https://ccnubox.muxixyz.com/api/ios/calendar/")
#    statu20 = resp20.status_code
#    r.set(url20,statu20)

#闪屏
@celery.task(name='start')
def start():
    resp21 = requests.get("https://ccnubox.muxixyz.com/api/start/")
    statu21 = resp21.status_code
    r21.set(i,statu21)


#IOS用户反馈
@celery.task(name='feedback')
def feedback():
    resp22 = requests.get("https://ccnubox.muxixyz.com/api/feedback/",\
                            headers = {"Authorization":"Basic %s" %b64admin})
    statu22 = resp22.status_code
    r22.set(i,statu22)
    
#获取IOS json数据
@celery.task(name='config_ios')
def config_ios():
    resp23 = requests.get("https://ccnubox.muxixyz.com/api/ios/config/")
    statu23 = resp23.status_code
    r23.set(i,statu23)

#木犀产品展示
@celery.task(name='product')
def product():
    resp24 = requests.get("https://ccnubox.muxixyz.com/api/product/")
    statu24 = resp24.status_code
    r24.set(i,statu24)


@celery.task(name='controli')
def controli():
    global i
    if i<TOTAL-1:
        i = i + 1
    elif i==TOTAL-1:
        i = 0
     
        


@app.route("/")
def index():
    return jsonify({
            "信息门户登录":[r01.get(k) for k in range(144)],
            "登录图书馆":[r02.get(k) for k in range(144)],
            "查询图书":[r03.get(k) for k in range(144)],
            "图书详情":[r04.get(k) for k in range(144)],
            "我的图书馆":[r05.get(k) for k in range(144)],
            "查询课表":[r06.get(k) for k in range(144)],
            "添加课程":[r07.get(k) for k in range(144)],
            "添加课程IOS":[r08.get(k) for k in range(144)],
            "删除课程":[r09.get(k) for k in range(144)],
            "编辑课表":[r10.get(k) for k in range(144)],
            "空调电费":[r11.get(k) for k in range(144)],
            "照明电费":[r12.get(k) for k in range(144)],
            "成绩查询":[r13.get(k) for k in range(144)],
            "部门信息":[r14.get(k) for k in range(144)],
            "常用网站":[r15.get(k) for k in range(144)],
            "通知公告":[r16.get(k) for k in range(144)],
            "获取Banner":[r17.get(k) for k in range(144)],
            "获取BannerIOS":[r18.get(k) for k in range(144)],
            "校历":[r19.get(k) for k in range(144)],
            "闪屏":[r21.get(k) for k in range(144)],
            "用户反馈IOS":[r22.get(k) for k in range(144)],
            "获取IOSJson数据":[r23.get(k) for k in range(144)],
            "木犀产品展示":[r24.get(k) for k in range(144)],
            })
if __name__ =='__main__':
    app.run(debug=True)
