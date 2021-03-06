import os
BASE_DIR=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #开启CSRF保护
    CSRF_ENABLED=True
    #设置密匙
    SECRET_KEY='123456'
    #格式为mysql+pymysql://数据库用户名：密码@数据库地址：端口号/数据库名称？数据库格式
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@localhost:3306/flaskblog?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS=False