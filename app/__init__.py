#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')

    register_buleprint(app)

    db.init_app(app)
    db.create_all(app=app)
    # with app.app_context():
    #     db.create_all()
    return app


def register_buleprint(app):
    from app.web import web
    app.register_blueprint(web)
