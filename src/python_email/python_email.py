# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import poplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header


POP3_ADDR = 'pop.163.com'
SMTP_ADDR = 'smtp.163.com'
USERNAME = 'fgwimcqxem38075@163.com'
PASSWORD = 'sagu1474'
# 以上账号信息仅作为演示使用，请勿滥用


def get_mail(index=1):
    '''获取指定序号的邮件，你或许应该先了解了解现在收件箱总共有多少邮件'''
    mail_server = poplib.POP3(POP3_ADDR)
    mail_server.user(USERNAME)
    mail_server.pass_(PASSWORD)
    # 登陆

    print(mail_server.stat()[0])
    # 获取收件箱现有的邮件数
    (resp, lines, octets) = mail_server.retr(index)
    # 获取第n封邮件，注意下标是从1开始的。
    # 返回的lines是一个列表，代表每一行信息，使用utf-8编码
    msg_lines = []
    for l in lines:
        msg_lines.append(l.decode('utf-8'))
    msg = '\n'.join(msg_lines)
    ''' 此处我们直接返回了原始的邮件数据，里面有很多我们不感兴趣的信息，
        比较好的做法是使用email模块中的相关工具进行解析，
        按照需求，解析出标题、正文、收件人信息等，甚至是附件。
    '''
    # print(msg)
    mail_server.quit()
    # 别忘了关闭连接
    return msg


def send_mail(msg, mail_to_addr='fgwimcqxem38075@163.com'):
    ''' 注意的是，这里的msg并不是普通的字符串，而是一个特殊的对象，
        详情可以参考后边的代码。
    '''
    mail_server = smtplib.SMTP(SMTP_ADDR)
    mail_server.login(USERNAME, PASSWORD)
    mail_server.sendmail(USERNAME, [mail_to_addr], msg.as_string())
    # 发送邮件，由于可以发送给多人，因此第二个参数是一个列表。
    mail_server.quit()


if __name__ == '__main__':
    print(get_mail())

    msg = MIMEText('this is the content', 'plain', 'utf-8')
    msg['Subject'] = Header('hello world!', 'utf-8')
    # 上面我们设置了邮件的正文和标题。
    # 一封标准的邮件还有其他组成部分，你可以补全它们。
    send_mail(msg)
