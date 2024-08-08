# -*-  coding : utf-8 -*-
# @Time : 2024/8/7 下午6:01
# @Autor : LceAn
# @File : main.py
# @Software : PyCharm


from app.models import *
from flask import render_template, request, jsonify



def init_route(app):
    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/api/localhost', methods=['GET'])
    def get_localhost():
        localhost_info = get_localhost_info()
        return jsonify(localhost_info)


    @app.route('/api/containers', methods=['GET'])
    def list_containers():
        container_info = get_container_info()
        return jsonify(container_info)
