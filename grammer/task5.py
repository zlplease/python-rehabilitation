# 1. 设计⼀个对象类（是时候创建一个自己的对象了），要求：
# 具有公有数据成员：姓名、性别
# 具有私有数据成员：年龄、金钱、电话、地址、学历
# 具有的公有成员函数
# 让对象说话（在控制台输出一句话）的函数talk
# 让对象买礼物的函数buy（金钱要对应地减少）
# 显示对象信息的函数display
# 设置对象信息的函数setdata
# 还想要对象有什么功能可以自由定制
import random

class lwdd:

    def setdata(self, name, sex, age, money, phone, address, degree):
        self.name = name
        self.sex = sex
        self.__age = age
        self.__money = money
        self.__phone = phone
        self.__address = address
        self.__degree = degree
        self.__saying = ['林炜秃了','林炜是大秃子','林炜是大大大大大秃子好耶']
    
    def talk(self):
        print(random.choice(self.__saying))

    def buy(self, cost):
        self.__money -= cost
    
    def display(self):
        print(self.name, self.sex)
        print(self.__age, self.__money, self.__phone, self.__address, self.__degree)

# 创建一个马老师类（继承第一题的类），调用talk函数之后会从马老师经典语录库中随机输出一
# 句
class lwgg(lwdd):
    pass

lw = lwgg()
lw.setdata('林炜','woman',19,1,'10086','sky','university')
lw.talk()