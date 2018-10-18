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


# # Question 23
# def square(num):
#     res = num**2
#     return res
# num=int(input('Write a number: '))
# print('result: '+str(square(num)))

# # Question 24
# import os
# print(abs.__doc__)
# print(filter.__doc__)
# print(map.__doc__)

# # Question 25
# class Dog:
#     name='Dog'
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind=kind
#
# dg = Dog('Martin', 'no')
# print(Dog.name +"  "+ dg.name)

# # Question 26
# def sum(a,b):
#     sum =  a+b
#     return sum
# print(sum(3,4))

# # Question 27
# def itos(i):
#     s=''
#     s=str(i)
#     print(s)
# itos(5)

# # Question 28
# def sum(a,b):
#     sum = int(a)+int(b)
#     print(sum)
#
# st= input("Write string of numbers ").split(' ')
# sum(st[0],st[1])


# # Question 29
# def concat(a,b):
#     res = a+b
#     print(res)
#
# st= input("Write string").split(' ')
# concat(st[0],st[1])

# # Question 30
# s1 = input('Write string 1')
# s2 = input('Write string 2')
# print(max(len(s1), len(s2)))
# if((len(s1)==len(s2))): print(s1+"\n"+s2)
# elif((len(s1)>len(s2))):print(s1)
# else: print(s2)

# # Question 31 and 32, 33,34
# def diction():
#     d = dict()
#     for i in range(1,4):
#         d[i] = i**2
#     print(d)
#     for (k,v) in d.items():
#             print(v)
#             # print(k)
# diction()

# # # Question 35, 36, 37,38,39
# def l():
#     l=list()
#     for i in range(1,21):
#         l.append(i**2)
#     # print all values from list
#     # print(l)
#     # print first 5 values from list
#     # print(l[:5])
#     # print last 5 values from list
#     # print(l[-5:])
# #     print all values except the first 5 elements in the list
# #     print(l[5:])
# create tuple from a list
#     t=tuple(l)
#     print(t)
#
# l()

# #Question 40,41
# tuple1=(1,2,3,4,5,6,7,8,9,10)
# l1=list()
# for i in tuple1:
#     if(i%2==0):
#         l1.append(i)
# # even values in tuple
# t1=tuple(l1)
# print(t1)
# # print first 5 and last 5 values
# # print(tuple[0:5])
# # print(tuple[5:])

# # Question 42
# s = input()
# st = {'YES', 'yes', 'Yes','YEs','yES','yeS'}
# if((s in st)==True):
#     print('Yes')
# else: print("No")


# # Question 43
# l = [1,2,3,4,5,6,7,8,9,10]
# r = filter(lambda x: x % 2 == 0, l)
# res = list(r)
# print(res)

# # Question 44
# l = [1,2,3,4,5,6,7,8,9,10]
# r = map(lambda x: x**2,l)
# res =list(r)
# print(res)

# #Question 45
# l = [1,2,3,4,5,6,7,8,9,10]
# r = map(lambda x: x**2,filter(lambda x: x % 2 == 0, l))
# res =list(r)
# print(res)

# # Question 46
# l = [1,2,3,4,5,6,7,8,9,10,50, 24, 12,74]
# r = filter(lambda x: x<20, filter(lambda x:x%2==0,l))
# res =list(r)
# print(res)

# # Question 47, 48
# class American:
#     @staticmethod
#     def printNationality():
#         print('American')
#
# # am = American()
# # am.printNationality()
#
# class NewYorker(American):
#     pass
# nyk = NewYorker()
# print(nyk.printNationality())

# # Question 49
# class Circle():
#     def calcares(self,radius):
#         self.radius = radius
#         rad = 3,14*radius**2
#         return rad
# circle = Circle()
# print(circle.calcares(8))

# # Question 49.1
# class Circle():
#     def __init__(self,rad):
#         self.rad = rad
#
#     def calcrad(self):
#         radius = 3,14*self.rad**2
#         return radius
# circle = Circle(8)
# print(circle.calcrad())

# # Question 50
# class Rectangle(object):
#     def __init__(self,l,w):
#         self.l = l
#         self.w = w
#
#     def area(self):
#         area = self.w*self.l
#         return(area)
# rect = Rectangle(2,5)
# print(rect.area())

# # Question 51
# class Shape(object):
#     def __init__(self):
#         pass
#
#     def area(self):
#         return 0
#
# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l
#
#     def area(self):
#         return self.length*self.length
#
# aSquare= Square(3)
# print(aSquare.area())


# Question 52
# try:
#     res = 5%0
# except :
#     raise RuntimeError('Division by 0')

#Question 53
# def divis(a,b):
#     return a%b
# try:
#     divis(5,0)
# except:
#     raise ZeroDivisionError('Change arguments of divis')

# # Question 56, 57
# s = input("Write an email: ").split('@')
# username = s[0]
# orgname = s[1].split('.')[0]
# print(username)
# print(orgname)


# # Question 58
# import re
# s = input('Write a string:').split(' ')
# l = list()
# for i in s:
#     m = re.findall('\d+', i)
#     l.append(m)
# print(l)

# # Question N
# import random
# l = list()
# for i in range(0,96):
#     r = random.uniform(0,1)
#     l.append(r)
#     print(r)
# l1 = l.sort()
# print(l1)

# # Question 59
# s = input()
# s1 = u"s"
# print(s1)

# # Question 61
# d = int(input())
# sum = 0
# for i in range(1,d+1):
#     res = i / (i+1)
#     sum += res
# print(sum)

# # Question 62
# def f(n):
#     if(n==0):
#         return 0
#     else:
#         return f(n-1) + 100
#
# n=int(input())
# print(f(n))

#Question 63
# def f(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# n = int(input())
# l =list()
# for i in range(0, n+1):
#     l.append(i)
# print(l)

# Question 64
# def generator(n):
#     for i in range(0, n+1):
#         if(i%5 ==0 and i%7==0):
#             yield i
# n = int(input())
# generator(n)
# res = []
# for i in generator(n):
#     res.append(str(i))
# print(",".join(res))


# Question 65
# l=[2,4,6,8,9]
# for i in l:
#     assert(i%2==0),'Number is not even'

#Question 66
# n = input()
# res = eval(n)
# print(res)

# Question 67
# def bsearch(l,n,low, high):
#     half = l[(low + high) // 2]
#     if (n == half):
#         print("result " + str(l.index(half)))
#     elif (n < half):
#         high = l.index(half) - 1
#         # print(l)
#         bsearch(l, n, low, high)
#     else:
#         low = l.index(half) + 1
#         # print(l)
#         bsearch(l, n, low, high)
#
# n = int(input())
# l =[0,1,3,7,8,4,5,9,6,2]
# l.sort()
# low = 0
# high = len(l)-1
# # half = l[(low+high)//2]
# print(l)
# bsearch(l,n,low,high)

# Question 68
# import random
# print(random.uniform(1,100))
# print(random.random()*100)


# Question 69
# import random
# print(random.uniform(5,95))


# Question 70
# import random
# print(random.choice([i for i in range(11) if i%2 ==0]))

# Question 71
# import random
# print(random.choice([i for i in range(11) if i%2 ==0]))

# Question 72
# import random
# print(random.sample(range(1,100),5))
# # even numbers
# print(random.sample([i for i in range(1,100) if i%2==0],5))
# # number div 7 and 5
# print(random.sample([i for i in range(1,201) if i%5==0 and i%7==0],5))


# Question 73
# import random
# print(random.randrange(7,16))

# Question 74
# import timeit
# t = timeit.Timer('1+1')
# print(t.repeat(10))

# Question 75
# import random
# l = [10,14,2,5,88,9,17,54,31,84,92,70,10,23]
# random.shuffle(l)
# print(l)
# sl = [3,6,7,8]
# random.shuffle(sl)
# print(sl)

#Question 76
# subject =['I', 'You']
# verb = ['play', 'love']
# object = ['football', 'hockey']
# for i in subject:
#     for j in verb:
#         for o in object:
#             print(i+' '+' '+j+' '+o)

# Question 77
# l = [5,6,77,45,22,12,24]
# res = [i for i in l if i%2==0]
# print(res)

# Question 78
# l = [12,24,35,70,88,120,155]
# nl = [i for i in l if i%5!=0 and i%7!=0]
# print(nl)

# Question 79
# l = [12,24,35,70,88,120,155]
# res = [v for (i,v) in enumerate(l) if i%2==0]

# # Question 80
# l = [[[0 for g in range(8)]for j in range(5)] for i in range(3)]
# print(l)

#Question 81
# l = [12,24,35,70,88,120,155]
# # nl = [v for (i,v) in enumerate(l) if i not in (0,4,5)]
# # print(nl)

#Question 82
