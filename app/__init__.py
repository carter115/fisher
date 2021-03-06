#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from app.models.book import db

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    # app = Flask(__name__, static_url_path='', static_folder='')
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    register_buleprint(app)

    db.init_app(app)
    db.create_all(app=app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    return app


def register_buleprint(app):
    from app.web import web
    app.register_blueprint(web)
