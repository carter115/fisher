#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wtforms import Form, IntegerField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, NumberRange, Email


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮件不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])

    nickname = StringField(validators=[DataRequired(),
                                       Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])
