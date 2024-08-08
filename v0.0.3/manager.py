# -*-  coding : utf-8 -*-
# @Time : 2024/8/7 下午5:58
# @Autor : LceAn
# @File : manager.py
# @Software : PyCharm


from flask import Flask
from app import initapp

app = initapp()

if __name__ == '__main__':
    app.run(debug=True)