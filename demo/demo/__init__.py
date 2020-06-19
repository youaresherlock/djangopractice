# 安装新的数据库驱动: PyMySQL. 替换原有的数据库驱动: mysqldb
from pymysql import install_as_MySQLdb

install_as_MySQLdb()