# !/usr/bin/python
# -*- coding: utf-8 -*-
from ..main import app
import logging

logger = logging.getLogger('django')


@app.task(name='send_email')
def send_email(to_email, verify_url):
    subject = 'email validate'
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用我们的产品。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
    send_email(subject, '', setting.EMAIL_FROM, [to_email]. html_message==html_message)

