# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：fixture和parametrize结合的参数化
import pytest
test_param = [(1,2), ("a","b"), (False,False), (int,int)]


@pytest.fixture()
def fixturefun(request):
    test = request.param
    return test


@pytest.mark.parametrize("fixturefun", test_param, indirect=True) # indirect=True，声明fixturefun不是参数，而是一个函数。
def test_case(fixturefun):
    assert fixturefun[0] == fixturefun[1]
