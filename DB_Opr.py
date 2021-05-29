import sqlite3


def add_data(name, message, image):
    sql = """
    INSERT INTO Social(name, message, image) VALUES('%s', '%s', '%s')""" % (name, message, image)
    execute_query(sql)


def get_chat():
    sql1 = """
    SELECT name FROM Social"""
    sql2 = """
    SELECT message FROM Social"""
    sql3 = """
    SELECT image FROM Social"""
    name = execute_query(sql1)
    message = execute_query(sql2)
    image = execute_query(sql3)
    return [n[0] for n in name.fetchall()], [m[0] for m in message.fetchall()], [i[0] for i in image.fetchall()]


def delete_chat():
    sql = """
    DELETE FROM Social"""
    execute_query(sql)


def execute_query(sql_query):
    with sqlite3.connect("chat.db") as conn:
        cur = conn.cursor()
        result = cur.execute(sql_query)
        conn.commit()
    return result
