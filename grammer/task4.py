# 1. 用eval()函数将字符串“{’name‘: ’xiaoming‘}”转化为字典对象。
# a = "{'name': 'xiaoming'}"
# b = eval(a)

# print(b)

# 2. 请定义一个函数计算一元二次方程的解，并根据解的个数返回不同的结果。
# import math

# def solve(a, b, c):
#     temp = b*b-4*a*c
#     if(temp<0):
#         result = [0]
#     else:
#         answer1 = (-b+math.sqrt(temp))/2*a
#         answer2 = (-b-math.sqrt(temp))/2*a
#         if(answer1 == answer2):
#             result = [1, answer1]
#         else:
#             result = [2, answer1, answer2]

#     return result

# print(solve(1,8,6))

#3. 请设计一个函数，可计算多个实数相加/减/乘/除。默认为计算多个实数相加。
# def solve(a, b, op=0):
#     if(op==0):
#         return a+b
#     elif(op==1):
#         return a-b
#     elif(op==2):
#         return a*b
#     elif(op==3):
#         if(b==0):
#             print("被除数不能为0")
#         else:
#             return a/b
    
# print(solve(1,0,3))

#4. 请设计一个函数，输入一个人的姓名，年龄，以及其他未知信息。将这些信息打印出来
def show_info(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

show_info('aaa', 19, grade="19", major="cs")

#请设计一个函数，计算汉诺塔问题
#好耶选做==不做