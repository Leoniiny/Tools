# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
#!/usr/bin/env python


def test_getini(pytestconfig):
    base_url = pytestconfig.getini("base_url")
    print("\n获取到ini文件参数 ：%s" % base_url)
