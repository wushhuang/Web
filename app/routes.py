from flask import render_template,flash,redirect,url_for
#页面返回的问题
from flask import request
from werkzeug.urls import url_parse
from app import app
#导入表单处理方法
from app.forms import LoginForm
#导入登录插件
from flask_login import current_user,login_user,logout_user
from flask_login import login_required
from app.models import User
#注册插件
from app import db
from app.forms import RegistrationForm

#建立路由
@app.route('/')
@app.route('/index')
#必须登录才能访问首页
#@login_required
def index():
    user={'username':'一方通行'}
    posts=[
        {
            'author':{'username':'刘'},
            'body':'这是模块循环一'
        },
        {
            'author':{'username':'小强'},
            'body':'这是模块循环2'
        }
    ]
    return render_template('index.html',title='首页',user=user,posts=posts)

@app.route('/register',methods=['Get','POST'])
def register():
    #判断当前用户是否验证，如果通过的话返回首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form =RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你成为我站的新用户！')
        return redirect(url_for('login'))
    return render_template('register.html',title='注册',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    #判断当前用户是否验证，通过的返回首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    #创建一个表单实例
    form=LoginForm()
    #验证表格数据格式
    if form.validate_on_submit():
        #根据表格里的数据进行查询，如果查询到数据返回User对象，否则返回None
        user=User.query.filter_by(username=form.username.data).first()
        #判断用户不存在或者密码不正确
        if user is None or not user.check_password(form.password.data):
            #如果不存在或者密码不正确，会提示这条信息
            flash('用户不存在或者登陆密码错误')
            return redirect(url_for('login'))
        #当用户名和密码都正确时来解决记住用户是否记住登录状态
        login_user(user,remember=form.remember_me.data)
        #此时的next_page记录的是跳转至登录页面时的地址
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc !="":
            next_page=url_for('index')
        #要么重定向至跳转前的页面，要么跳转到首页
        return redirect(next_page)
    return render_template('login.html',title='登录',form=form)
#登出模块
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))