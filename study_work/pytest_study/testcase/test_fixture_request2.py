# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信公众号：AllTests软件测试
"""

import pytest

@pytest.fixture(scope="session")
def my_fixture1():
    aaa = "AllTests软件测试"
    return aaa

@pytest.fixture(scope="session")
def my_fixture2():
    bbb = "1234567890"
    return bbb

@pytest.fixture(scope="session", params=["my_fixture1", "my_fixture2"])
def get_fixture_value(request):
    ccc = request.getfixturevalue(request.param)
    return ccc

def test_case(get_fixture_value):
    print("\n获取到的fixture值：" + get_fixture_value)
