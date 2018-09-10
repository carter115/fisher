#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import mail
from flask_mail import Message
from flask import current_app, render_template


# def send_mail():
#     msg = Message('测试邮件', sender=current_app.config['MAIL_USERNAME'],
#                   body='Test', recipients=['aaa@qq.com'])
#     mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    subj = current_app.config['MAIL_SUBJECT_PREFIX'] + ' ' + subject
    sender = current_app.config['MAIL_USERNAME']

    msg = Message(subj, sender=sender, recipients=[to])
    msg.html = render_template(template, **kwargs)

    mail.send(msg)
