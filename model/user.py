# -*- coding: utf-8 -*-
from flask import session
class User:
    def getUserName(self):
        if self.id==1:
            name="wanghaotian"
        else:
            name="游客"
        return name
    def checkLogin(self,username,password):
        if username=="wang" and password=="wang":
            session['username']=username
            return session['username']
        else:
            return "Hello Python!~"
