import pymysql
from config.settings import DB_CONFIG
from utils.logutil import logger

class MysqlUtil:
    def __init__(self):
        # 读取配置文件，初始化pymysql数据库连接
        self.db = pymysql.connect(**DB_CONFIG)
        # 创建数据库游标
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    # 获取单条数据
    def get_fetchone(self, sql):
        self.cursor.execute(sql)
        # 查询单条数据结果返回
        return self.cursor.fetchone()

    # 获取多条数据
    def get_fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 执行更新类sql
    def sql_execute(self, sql):
        try:
            # db对象和游标对象同时存在
            if self.db and self.cursor:
                # 执行sql
                self.cursor.execute(sql)
                # 提交执行sql到数据库，完成insert或者update相关操作
                self.db.commit()
        except Exception as e:
            # 出现异常，数据库回滚
            self.db.rollback()
            # 打印日志
            logger.error("sql语句执行错误，已执行回滚操作")
            # 返回结果为失败
            return False

    # 关闭对象，staticmethod静态方法，可以直接使用类名.静态方法
    @staticmethod
    def close(self):
        # 判断游标对象是否存在
        if self.cursor is not None:
            # 如果存在，则关闭指针
            self.cursor.close()
        # 判断数据库对象是否存在
        if self.db is not None:
            # 如果存在，则关闭对象
            self.db.close()

# 测试代码
if __name__ == '__main__':
    mysql = MysqlUtil()
    res = mysql.get_fetchall("select * from test_case_list")
    print(res)

