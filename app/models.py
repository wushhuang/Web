from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login
#用户加载函数
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


#添加数据库表 User
class User(UserMixin,db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(128))
    #back是反向引用，user和post是一对多的关系，backref是表示再post中新建一个属性author,关联的是post中user_id外键关联的user对象。
    #lazy属性常用的值含义，select就是访问到属性的时候，会全部加载该属性的数据。
    posts=db.relationship('Post',backref='author',lazy='dynamic')
    def __repr__(self):
        return '<用户名:{}>'.format(self.username)
    #密码加密函数
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    #加密对比函数
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    

#添加数据库表Post
class Post(db.Model):   
    __tablename__='post'
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String(140))
    timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Post{}>'.format(self.body)