# !/usr/bin python3                                 
# encoding: utf-8 -*-
# @Function：conftest.py学习
import pytest
from study_work.pytest_study.business.get_token import GetToken


@pytest.fixture(scope='session',autouse=True)
def get_token():
    token = GetToken().get_token()
    return token


if __name__ == '__main__':
    GetToken().get_token()