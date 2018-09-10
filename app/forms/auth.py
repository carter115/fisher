#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wtforms import Form, IntegerField, StringField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, NumberRange, Email, EqualTo
from app.models.user import User


class Emailform(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮件不符合规范')])


class LoginForm(Emailform):
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])


class RegisterForm(LoginForm):
    nickname = StringField(validators=[DataRequired(),
                                       Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class ResetPasswordForm(Form):
    password1 = PasswordField(
        validators=[DataRequired(),
                    Length(6, 32, message='密码长度至少需要6到32个字符之间'),
                    EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField(validators=[DataRequired(), Length(6, 32)])
