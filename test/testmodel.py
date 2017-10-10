from model import DB
from model import Tuser
dbconn=DB()
session=dbconn.dbconnect()
print(session)
new_user = Tuser(id='12', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()