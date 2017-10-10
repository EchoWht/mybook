# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Tuser(Base):
    # 表的名字:
    __tablename__ = 'tuser'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
class DBConn:
    def dbconnect(self):
        engine = create_engine('mysql+mysqlconnector://zhangyiwen:zyw1234@localhost:3306/test')
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建Session:
        session = DBSession()
        return session
# dbconn=DBConn()
# session=dbconn.dbconnect()
# print(session)
# new_user = Tuser(id='3', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()