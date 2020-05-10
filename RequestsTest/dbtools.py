import pymysql

def chaxun(sql):
    #数据库连接
    db = pymysql.connect (host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb")
    # 游标
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    return res
