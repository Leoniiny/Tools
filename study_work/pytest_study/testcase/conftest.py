import pytest
import yaml
import os

import pytest


# 方式1：通过 pytestconfig 获取命令行参数配置
@pytest.fixture
def cmd_param(pytestconfig):
    return pytestconfig.getoption("--define")


# 方式2：通过 request.config 获取命令行参数配置
@pytest.fixture
def request_param(request):
    params = request.config.getoption("--cmdopt")
    return params


# 注册命令行参数
def pytest_addoption(parser):
    parser.addoption(
        "--define",  # 规范写法： --自定义参数
        action="store",
        default="https://www.baidu.com",  # 默认值，在调用这个参数时，不传值时使用
        help="test base define"  # 自定义参数说明
    )
    parser.addoption(
        "--cmdopt",  # 规范写法： --自定义参数
        action="append",
        default=["二狗","adc","jug"],  # 默认值，在调用这个参数时，不传值时使用
        help="test base cmdopt"  # 自定义参数说明
    )
