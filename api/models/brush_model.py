# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    xingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )

class shouji(Base_model):
    __doc__ = u'''shouji'''
    __tablename__ = 'shouji'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='标题' )
    laiyuan=db.Column( db.Text,  nullable=True, unique=False,comment='来源' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    jiage=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='价格' )
    pinpai=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='品牌' )
    spcd=db.Column( db.Text,  nullable=True, unique=False,comment='商品产地' )
    yxnc=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='运行内存' )
    jsys=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='机身颜色' )
    jsnc=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='机身内存' )
    hszxs=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='后摄主像素' )
    fengge=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='风格' )
    xiaoliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    comment=db.Column( db.Text,  nullable=True, unique=False,comment='评论' )

class systemintro(Base_model):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

