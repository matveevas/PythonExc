#Question 1
#a = list(range(2000, 3200))
#print(a)
#b = list()
#for i in a:
#    if(i%7==0 and i%5!=0):
#        b.append(i)
#        #print(i)
#print(b)

# #Quetion 2
# s = input("Write a value: ")
# a = list(range(1,int(s)+1))
# b=list()
# print(a)
# res= 1
# for i in a:
#     res= i*res
#     b.append(res)
# print(b)

# #Quetion 3
# s = input("Write a value: ")
# # d = dict(a: a**2 for a in range(int(s)+1))
# dq=dict()
# a=list(range(1,int(s)+1))
# print(a)
# for i in a:
#     dq[i]=i*i
# print(dq)

# # Question 4
# s = input("Write a value: ").split(',')
# print(s)
# l = list()
# l.append(s)
# t = tuple(l)
# print(l)
# print(type(l))
# print(t)
# print(type(t))


# # Question 5
# class NCl:
#     def __init__(self): self
#
#     def getString(self):
#         self.s = input("Write value: ")
#
#     def printString(self):
#         print("Input value: "+self.s.upper())
#
#
# obj = NCl()
# obj.getString()
# obj.printString()

# # Question 6
# import math
# c = 50
# h = 30
# d = input("Write a value: ").split(',')
# res = list()
# print(d[0])
# for i in d:
#     res.append(round(math.sqrt((2*int(i)*c)/h)))
# print(res)

# # # Question 8
# str = input("Write string: ").split(",")
# print(type(str))
# str.sort()
# print(str)
# print(type(str[0]))

# # Question9
# str = input("Write a string: ")
# res = ""
# for i in str:
#      res = res+i.capitalize()
# print(res)

# # Question 10
# s = set()
# str = input("Wirte a string: ").split(" ")
# for i in str:
#     s.add(i)
# res = list(s)
# res.sort()
# print(res)

# # Question 11
# dg = input("Write a digits: ").split(",")
# l=list()
# for i in dg:
#     res = int(i, 2) % 5
#     if (res==0):
#         l.append(i)
# print(l)

# # Question 12
# str = input("Write a digits: ").split(",")
# l=list()
# for i in str:
#     res = int(i)%2
#     if (res ==0):
#         l.append(int(i))
# print(l)


# # Question 13
# import re
# str1 = input("Write a string: ")
# l = 0
# d = 0
# for i in str1:
#     res = re.findall('\d', str1)
#     let = re.findall('[a-zA-Z]', str1)
# print(let)
# print("Digits: " + str(len(res)))
# print("Letters: " + str(len(let)))

# # Question 13
# str1 = input("Write a string: ")
# up =0
# lw =0
# for i in str1:
#     if (i.isupper()):
#         up+=1
#     else:
#         if(i.islower()==True):
#             lw+=1
# print("Upper case"+str(up))
# print("Lower case"+ str(lw))

# # Question 15
# str1 = input("Write a digit: ")
# f=""
# s=""
# t=""
# res = int(str1)+int(str1+str1)+int(str1+str1+str1)+int(str1+str1+str1+str1)
# print(res)

# # Question 16
# str1 = input("Write digits: ").split(",")
# l = list()
# for i in str1:
#     if(int(i)%2!=0):
#         l.append(i)
# print(l)

# # Question 17
# amount = 0
# while True:
#     str1 = input("Write digits: ")
#     if not str1:
#         break
#     str2 = str1.split(" ")
#     oper = str2[0]
#     print(str2)
#     val = int(str2[1])
#     if oper=="D":
#         amount+=val
#     elif oper=="W":
#         amount-=val
#     else :
#         pass
# print("Amount: "+amount)

# # Question 18
# import re
# str1 = input("Write a password: ").split(",")
# l = list()
# res = 0
# for i in str1:
#    if(len(i)>6 and len(i)<12):
#        if (re.search('[a-z]',i)) :
#            res+=1
#            if (re.search('[A-Z]',i)):res+=1
#            if (re.search('\d',i)): res+=1
#            if (re.search('[$#@]',i)):res+=1
#            if(res==4): l.append(i)
#            continue
#    else:
#        pass
# print(l)


# # Question 19
# from operator import itemgetter, attrgetter
# tup = ()
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(',')))
# print(sorted(l, key=itemgetter(0, 1, 2)))


# # Question 20?????
# def putNumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
#
# for i in reversed(100):
#     print(i)


# # Question21
# import math
# l=list()
# x=0
# y=0
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(s.split('\n'))
#     for i in l:
#         # print(type(i))
#         for j in i:
#             a = str(j).split(' ')
#             # print(a[0])
#     if(a[0]=='UP'): x+= int(a[1])
#     if(a[0]=='DOWN'): x-=int(a[1])
#     if (a[0] == 'RIGHT'): y += int(a[1])
#     if (a[0] == 'LEFT'): y -= int(a[1])
#     res = math.floor(math.sqrt(math.pow(x, 2)+math.pow(y, 2)))
# print(x)
# print(y)
# print(res)

# # Question22
# str = input("Write a string").split(' ')
# # print(str)
# words=dict()
# k=0
# s=set()
# for i in str:
#     s.add(i)
#     words[i]=0
# for i in str:
#     if((i in s )== True):
#         words[i] += 1
# # print(s)
# print(words)


# Question 23












