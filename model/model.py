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
# 定义my_book
class MyBook(Base):
    __tablename__ = 'my_book'
    book_id = Column(String(11), primary_key=True)
    book_name = Column(String(100))
    book_author = Column(String(100))
    book_buy_date = Column(String(20))
    # book_translator = Column(String(100))
    book_price = Column(String(20))
    book_reading_progress = Column(String(3))

# 初始化数据库连接:
class DB:
    def dbconnect(self):
        engine = create_engine('mysql+mysqlconnector://zhangyiwen:zyw1234@localhost:3306/py_mybook')
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