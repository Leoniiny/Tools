# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：


def test_getoption1(pytestconfig):
    param = pytestconfig.getoption("--cmdopt")
    print("\ntest_getoption1的获取到命令行参数：%s" % param)
    # 如果返回值是个列表可以将值取出来，单独调用
    print("\ntest_getoption1的获取到命令行参数中的第一个值：%s" % param[0])

def test_getoption2(request_param):
    print("\ntest_getoption2的获取到命令行参数：%s" % request_param)
    print("\ntest_getoption2的获取到命令行参数：%s" % request_param[-1])


