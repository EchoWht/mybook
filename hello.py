import os
from flask import Flask,jsonify,render_template,session, redirect, url_for, escape, request
from model.user import User
from controller.controller import MyBookController
from router.router import IndexRoute
from router.router import BookRoute
from werkzeug import secure_filename

# 引入jd爬虫
from spider.spiderMan import Jd

UPLOAD_FOLDER = "static/file/"
# url_for(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 404page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('/error_page/404.html'), 404
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 上传
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

# 首页
@app.route('/')
def index():
    username = IndexRoute().index_page()
    return render_template('index.html',username=username)

# 登录
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user=User()
        user.checkLogin(username,password)
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

# 登出
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
# 所有图书列表
@app.route('/booklist')
def booklist():
    booklist = BookRoute().booklist_page()
    return  render_template("booklist.html",booklist=booklist)

# book详情
@app.route('/book/<int:id>')
def book(id):
    mybook= BookRoute().book_page(id)
    return render_template("book.html",mybook=mybook)
# addbook
@app.route('/addbook',methods=['POST','GET'])
def addbook():
    if request.method == 'POST':
        mession_done=BookRoute().addbook_post_page(id)
        return render_template("base/done.html", mession_done=mession_done)
    else:
        return render_template('addbook.html')
# 修改
@app.route('/updatebook/<int:id>',methods=['POST','GET'])
def updatebook(id):
    if request.method == 'POST':
        mession_done=BookRoute().updatebook_post_page(id)
        return render_template("base/done.html",mession_done=mession_done)
    else:
        mybook = BookRoute().book_page(id)
        return render_template('updatebook.html',mybook=mybook)
# 删除
@app.route('/delbook/<int:id>')
def delbook(id):
    mession_done = BookRoute().delbook_page(id)
    return render_template("base/done.html", mession_done=mession_done)
# 测试
@app.route('/test')
def test():
    username=IndexRoute().index_page()
    return username

# ajax

# ajax返回jd图书相关信息
@app.route('/_get_jdbook_info')
def get_jdbook_info():
    name = request.args.get('keywords', 0, type=str)
    book_price = Jd(name).getBookPrice()
    book_author=Jd(name).getBookAuthor()
    result={'book_price':book_price,'book_author':book_author}
    return jsonify(result=result)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
    app.run()