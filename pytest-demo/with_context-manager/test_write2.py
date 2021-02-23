import pymysql


def test_write():
    sql = """ """  # 具体的sql语句
    conn = DBConnection(0)
    with conn as cursor:
        cursor.execute(sql)


class DBConnection():
    def __init__(self, id):
        self.id = id

    def cursor(self):
        # 返回一个游标并且启动一个事务
        pass

    def commit(self):
        # 提交当前事务
        pass

    def rollback(self):
        # 回滚当前事务
        pass

    def __enter__(self):
        # 返回一个cursor
        cursor = self.cursor()
        return cursor

    def __exit__(self, typr, value, ex):
        if ex is None:
            # 没有异常则提交事务
            self.commit()
        else:
            # 有异常则回滚数据库
            self.rollback()

# 当with遇到上下文管理器，就会在执行语句体之前，先执行上下文管理器的__enter__方法，
# 然后再执行语句体，执行完语句体后，最后执行__exit__方法
# try-catch-finally的变种写法
