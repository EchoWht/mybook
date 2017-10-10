import sys
sys.path.append("..")
from model.model import DB
from model.model import Tuser
from model.model import MyBook
class TuserController:
    def adduser(self):
        dbconn = DB()
        dbsession = dbconn.dbconnect()
        print(dbsession)
        new_user = Tuser(id='122', name='mrBob')
        # 添加到session:
        dbsession.add(new_user)
        # 提交即保存到数据库:
        dbsession.commit()
        # 关闭session:
        dbsession.close()
class MyBookController:
    def __init__(self):
        dbconn = DB()
        dbsession = dbconn.dbconnect()
        self.dbsession=dbsession
    def addMyBook(self,book):
        new_book=MyBook(
                        book_id=book[0],
                        book_name=book[1],
                        book_author=book[2],
                        book_buy_date=book[3],
                        # book_translator=book[4],
                        book_price=book[4],
                        book_reading_progress=book[5],
                        )
        # self.dbsession.add(new_book)
        print ("------------>")
        print (self.dbsession.add(new_book))
        # 提交即保存到数据库:
        self.dbsession.commit()
        # 关闭session:
        self.dbsession.close()

    def getMyBookById(self,book_id):
        mybook = self.dbsession.query(MyBook).filter(MyBook.book_id == book_id).one()
        self.dbsession.close()
        return mybook
    def getMyBookList(self):
        mybook=self.dbsession.query(MyBook).limit(30).offset(2).all()
        print(self.dbsession.query(MyBook).count())
        return mybook
    def updateMyBookById(self,book):

        self.dbsession.query(MyBook).filter(MyBook.book_id == book['book_id']).update(book)

        self.dbsession.commit()
        self.dbsession.close()
    def deleteMyBookById(self,book_id):
        mybook=self.getMyBookById(book_id)
        self.dbsession.delete(mybook)
        self.dbsession.commit()
        self.dbsession.close()