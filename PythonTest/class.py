
# 新建一个类：
class Person():
    mingzi = "张三"   # 成员变量：类里面的变量：属性
    shenggo = 180
    tizhong = 100
    xingbie = "男"

    # 成员方法：类里面的方法
    # self：固定
    def pao(self):
        print("人可以跑")

# 调用类：实例化
p = Person()        # Person()实例化Person类，返回类对象并且赋值给p变量
print(p.mingzi)     # 调用属性
p.pao()             # 调用方法
