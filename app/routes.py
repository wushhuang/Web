from flask import render_template,flash,redirect,url_for
from app import app
#导入表单处理方法
from app.forms import LoginForm
#建立路由
@app.route('/')
@app.route('/index')
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

@app.route('/login',methods=['GET','POST'])
def login():
    #创建一个表单实例
    form=LoginForm()
    #验证表格数据格式
    if form.validate_on_submit():
        flash('用户登录的用户名是:{},是否记住我{}'.format(
            form.username.data,form.remember_me.data
        ))
        #重定向至首页
        return redirect(url_for('index'))
    return render_template('login.html',title='登录',form=form)