#第一题
# a = input().split()
# sum = 0

# for each in a:
#     if each.isdigit():
#         sum += int(each)

# print(sum)


#第二题
# import math

# def is_prime(n):
#     if(n==1):
#         return False
#     elif(n>1):
#         for i in range(2,int(math.sqrt(n))):
#             if(n % i == 0):
#                 return False

#     return True

# a = int(input())

# if(is_prime(a)):
#     print("yes")
# else:
#     print("no")


# 第三题
# a = input()
# letter = {}

# for i in range(0,len(a)):
#     letter.setdefault(i,a[i])

# print(letter)

list = []

for i in range(6):
    list.append(int(input()))

for i in range(6):
    min = i
    for j in range(i+1,6):
        if(list[min]>list[j]):
            min = j
    temp = list[i]
    list[i] = list[min]
    list[min] = temp

for i in range(6):
    print(list[i],end=' ')
    