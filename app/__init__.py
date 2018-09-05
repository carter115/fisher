#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_buleprint(app)
    return app


def register_buleprint(app):
    # from app.web.book import web
    from app.web import web
    app.register_blueprint(web)
