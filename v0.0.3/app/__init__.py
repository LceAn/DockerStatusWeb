# -*-  coding : utf-8 -*-
# @Time : 2024/8/7 下午5:58
# @Autor : LceAn
# @File : __init__.py.py
# @Software : PyCharm



from flask import Flask
from app.views import init_route

def initapp():
    app = Flask(__name__)
    init_route(app)
    return app