# 配置蓝图
from flask import Blueprint

# 蓝本的名字和蓝本所在的包或模块
get_latest = Blueprint('get_latest', __name__)

from . import views
