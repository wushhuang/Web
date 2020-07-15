from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
#用户加载函数
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
def load_post(username):
    u_id = User.query.filter_by(username=username).first.id
    return Post.query.filter_by(user_id=u_id).body

#添加数据库表 User
class User(UserMixin,db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)
    password_hash=db.Column(db.String(128))
    about_me=db.Column(db.String(140))
    last_seen=db.Column(db.DateTime,default=datetime.utcnow)
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
    #用户头像
    def avatar(self,size):
        digest=md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest,size)
    

#添加数据库表Post
class Post(db.Model):   
    __tablename__='post'
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String(140))
    timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Post{}>'.format(self.body)
#香客信息
class xiangke(UserMixin,db.Model):
    __tablename__='xiangke'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32))
    age=db.Column(db.Integer)
    jiguan=db.Column(db.String(140))
    zhiye=db.Column(db.String(32))
    dizhi=db.Column(db.String(140))
    dianhua=db.Column(db.Integer,index=True,unique=True)
    email=db.Column(db.String(120),index=True,unique=True)

class yuding(db.Model):
    __tablename__='yuding'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('xiangke.id'))
    timestamp=db.Column(db.DateTime)

class xiangmu(db.Model):
    __tablename__='xiangmu'
    id=db.Column(db.Integer,primary_key=True)
    cate=db.Column(db.String(32))

class xiangfang(db.Model):
    __tablename__='xiangfang'
    id=db.Column(db.Integer,primary_key=True)
    fanghao=db.Column(db.Integer,index=True,unique=True)
    info=db.Column(db.Integer,default=0)   #0 空闲 1预定 2入住


