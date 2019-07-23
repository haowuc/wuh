##################################
# demo:给出所有快捷键
##################################

##################################
# demo_conf:配置模板
# demo_import:导入模板
# demo_api:接口调用模板
# demo_tools:工具用法演示
##################################
from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf

def test_login():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = 'http://qa.yansl.com:8080/admin/login'
    req = {
        "password": "123456",
  "username": "admin"
    }
    resp = request_tool.post_request(url,json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['code'],2000)
    data =body['data']
    if data !='':
        token = data['token']
        assert_tool.assert_not_null(token)

##################################
# demo_conf_api：接口url地址模板
# demo_conf_db:数据库配置模板
##################################


##################################
# demo_import_api：接口测试导入模板
##################################

##################################
# demo_tools:工具包全部使用模板
# demo_tools_excel:excel工具使用模板
# demo_tools_mysql:mysql工具使用模板
# demo_tools_random:random工具使用模板
# demo_tools_log:log工具使用模板
# demo_tools_shell:shell工具使用模板
##################################

##################################
# demo_api_login：登陆接口模板（4种模板）
# demo_api_login：登陆接口模板-常量
# demo_api_login_var：登陆接口模板-变量
# demo_api_login_param：登陆接口模板-参数化（数据分离）
# demo_api_login_zuhe：登陆接口模板-组合使用（常量+变量+参数化）
##################################
