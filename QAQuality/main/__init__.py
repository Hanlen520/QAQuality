# 配置蓝图
from flask import Blueprint

# 蓝本的名字和蓝本所在的包或模块
main = Blueprint('main', __name__)

from . import views
