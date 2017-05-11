#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,make_response,render_template,request
from flask_restful import reqparse

web=Flask(__name__)

@web.route('/')
def login():
    return render_template("login.html")

@web.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html",login_data=request.form['uname'])

if __name__ == "__main__":
    web.run(debug=True)
