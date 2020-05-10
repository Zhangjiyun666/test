# 1.在F:\work_home\github\requesttest创建requesttest文件夹；
# 2.在vscode里点击文件，打开文件夹requesttest；
# 3.在文件夹里创建demo01.py；

# 导入requests
import requests

# get
url = "http://192.144.148.91:2333/get_title_img"   # 接口地址
res = requests.get(url)                  # http的get请求   
print (res.text)                         # res.text就是返回值的body


# post
url1 = "http://192.144.148.91:2333/login"
data = {"username":"liuyun1", "password":"a12345678"}
res1 = requests.post(url=url1, json = data)
print (res1.text)







