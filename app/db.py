from app import db
from app.models import User,Post
#构造一个实例对象
u=User(username='game',email='game@123.com')
#加载实例
db.session.add(u)
#提交
db.session.commit()

#查询数据库信息
#查询数据库中所有实例
users=User.query.all()
>>>users   #会显示对象数组
for u in users:
    print(u.id,u.username,u.post)

#外键关联一对多插入数据
u=User.query.get(4)
#构造实例，与User对象建立联系
p=Post(body='命令行提交数据1',author=u)
db.session.add(p)
db.session.commit()
#第二次插入数据
p=Post(body='命令行第二次提交',author=u)
db.session.add(p)
db.session.commit()

#外键关联一对多查询数据库
u=User.query.get(4)
posts=u.posts.all()
>>>posts

#对所有的posts进行查询
posts=Post.query.all()
for p in posts:
    print(p.id,p.author.username,p.body)

#按指定规则查询
User.query.order_by(User.username.desc()).all()
