#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import mail
from flask_mail import Message
from flask import current_app, render_template
from threading import Thread


# def send_mail():
#     msg = Message('测试邮件', sender=current_app.config['MAIL_USERNAME'],
#                   body='Test', recipients=['aaa@qq.com'])
#     mail.send(msg)

def send_async_mail(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    subj = current_app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject
    sender = current_app.config['MAIL_USERNAME']

    msg = Message(subj, sender=sender, recipients=[to])
    msg.html = render_template(template, **kwargs)

    app = current_app._get_current_object()
    # current_app只是代理核心对象Flask，多线程隔离情况下，需要拿取真实的Flask对象
    # thr = Thread(target=send_async_mail, args=[current_app, msg])
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
