# 导入requests
import requests
from dbtools import chaxun

# 构造请求
url = "http://192.144.148.91:2333/get_title_img"   # 接口地址
res = requests.get(url)                  # http的get请求 

# 判断结果 （1.判断http状态码；2.判断返回值>结果码）
assert res.status_code ==200          # 调用requests的status_code属性，获取http状态码
assert res.json().get("status") ==200 # 把返回值转换成python的字符串

# 查询数据库：接口返回值相关的信息
# 1.获取到每个轮播图的id

for r in res.json().get("data"):
    lid = r.get("id")

    # 2.再用sql去数据库查这些id 
    sql = "select * from t_title_img where id = {}".format(lid)  # 去数据库中查每条轮播图的信息
    res = chaxun(sql)         # res ((137, 'test555', None, '75UbhhZTcMwNLLz.jpg', 'https://images.unsplash.com/', 0, None, datetime.datetime(2020, 4, 22, 19, 10, 17), datetime.datetime(2020, 4, 22, 19, 10, 17)),)
    assert len (res) != 0     # 数据库查询的结果长度不为0

print ("成功了!")
