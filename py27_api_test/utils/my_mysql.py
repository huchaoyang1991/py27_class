import pymysql

from py27_api_test.utils.my_config import conf


class MyMysql:
    def __init__(self):
        """
        初始化连接池
        """
        # 建立连接
        self.con = pymysql.connect(host=conf.get("mysql", "host"),
                                   port=int(conf.get("mysql", "port")),
                                   user=conf.get("mysql", "user"),
                                   password=conf.get("mysql", "password"),
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor  # 声明返回字典类型
                                   )
        # 创建一个游标对象
        self.cur = self.con.cursor()

    def find_count(self, sql) -> int:
        """
        查询sql影响条数
        :param sql:sql语句
        :return: 返回影响条数
        """
        self.con.commit()
        return self.cur.execute(sql)

    def find_all(self, sql) -> list:
        """
        查询全部-sql
        :param sql: sql查询语句
        :return: 返回查询的所有数据
        """
        self.con.commit()

        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_one(self, sql) -> dict:
        """
        查询一条-sql
        :param sql: sql查询语句
        :return: 返回查询的一条数据
        """
        self.con.commit()

        self.cur.execute(sql)
        return self.cur.fetchone()

    def update(self, sql) -> None:
        """
        增删改
        :param sql: sql语句
        """
        self.cur.execute(sql)
        self.con.commit()


db = MyMysql()
