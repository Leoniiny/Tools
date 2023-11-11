# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import pytest
import smtplib
smtpserver = "mail.python.org"
new_str = '32141234'


@pytest.fixture(scope="module")
def my_smtp(request):
    # request.module属性从测试模块中获取smtpserver值。
    # server = getattr(request.module, "smtpserver", "smtp.163.com")
    # print("\nfixture 获取到的server >>>：%s" % server)
    # smtp = smtplib.SMTP(server, 587, timeout=5)
    # yield smtp
    # print("\n执行完毕 %s (%s)" % (smtp, server))
    # smtp.close()
    string = getattr(request.module, "new_str", "默认值")
    print("\nfixture string >>>：%s" % string)


def test_smtp(my_smtp):
    print("\n执行测试")
