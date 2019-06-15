
import pymysql
def test_write():
    con = pymysql.connections()
    cursor = con.cursor
    sql = """ """

    try:
        cursor.execute(sql)
        cursor.execute(sql)
        cursor.execute(sql)
        con.commit()    # 提交事务
    except Exception as ex:
        con.rollback()  # 事务执行失败


