from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length
from wtforms.validators import ValidationError,Email,EqualTo
from app.models import User

#'''用来处理登录信息的文件'''
class LoginForm(FlaskForm):
    #DataRequired,当你在当前表格没有输入而直接到下一个表格时会提示你输入
    username=StringField('用户名',validators=[DataRequired(message='请输入用户名')])
    password=PasswordField('密码',validators=[DataRequired(message='请输入密码')])
    remember_me=BooleanField('记住我')
    submit=SubmitField('登录')

#'''处理注册信息的文件'''
class RegistrationForm(FlaskForm):
    username=StringField('用户名',validators=[DataRequired()])
    email=StringField(validators=[DataRequired(),Email(message='电子邮箱不符合规范')])
    password=PasswordField('密码',validators=[DataRequired(message='密码太过简单')])
    password2=PasswordField(
        '重复密码',validators=[DataRequired(message='密码不一致'),EqualTo('password')]
    )
    submit=SubmitField('注册')
    #校验用户名是否重复
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名已存在，请更换！')
    #校验邮箱是否重复
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('该邮箱已被注册，请更换新的邮箱！')
    
    #校验密码
    def validate_password(self,password):
        if password.data is None:
            raise ValidationError('密码不能为空')

#'''修改个人信息'''
class EditProfileForm(FlaskForm):
    username=StringField('用户名',validators=[DataRequired(message='请输入用户名！')])
    about_me=TextAreaField('关于我',validators=[Length(min=0,max=140)])
    submit=SubmitField('提交')