# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：
import pytest

@pytest.fixture()
def fixturefun():
    return 123

def test_case(fixturefun):
    assert fixturefun == 123
