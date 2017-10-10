from flask import Flask,jsonify,render_template,session, redirect, url_for, escape, request
from controller.controller import MyBookController
from spider.spiderMan import Jd
class IndexRoute:
    def index_page(self):
        if 'username' in session:
            username = session['username']
        else:
            username = "Hello Python"
        return username
class BookRoute:
    def booklist_page(self):
        booklist = MyBookController().getMyBookList()
        for bookiteam in booklist:
            bookiteam.jdbook_pic_url = Jd(bookiteam.book_name).getBookImg()
        return booklist
    def book_page(self,id):
        mybook = MyBookController().getMyBookById(id)
        mybook.jdbook_pic_url = Jd(mybook.book_name).getBookImg()
        return mybook
    def addbook_post_page(self,data):
        book_id = ''
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        book_buy_date = request.form['book_buy_date']
        # book_translator =  request.form['book_translator']
        book_price = request.form['book_price']
        book_reading_progress = request.form['book_reading_progress']
        data = [book_id, book_name, book_author, book_buy_date, book_price, book_reading_progress]
        mybook = MyBookController().addMyBook(data)
        mession_done = "添加成功"
        return mession_done
    def updatebook_post_page(self,id):
        book_id = request.form['book_id']
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        book_buy_date = request.form['book_buy_date']
        # book_translator =  request.form['book_translator']
        book_price = request.form['book_price']
        book_reading_progress = request.form['book_reading_progress']
        data = {"book_id": book_id,
                "book_name": book_name,
                "book_author": book_author,
                "book_buy_date": book_buy_date,
                # "book_translator":book_translator,
                "book_price": book_price,
                "book_reading_progress": book_reading_progress
                }
        mybook = MyBookController().updateMyBookById(data)
        mession_done = "修改成功"
        return mession_done
    def delbook_page(self,id):
        mybook = MyBookController().deleteMyBookById(book_id=id)
        mession_done = "删除成功"
        return mession_done
