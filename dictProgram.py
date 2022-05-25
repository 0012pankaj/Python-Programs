# take input dictionary from youser
from ast import If
from ctypes.wintypes import SHORT
from operator import indexOf
from tkinter import E


# d={}
# x=int(input("Enter size="))
# for i in range(x):
#     k=int(input())
#     v=int(input())
#     d.update({k:v})
# print(d)


# for i in d:
#     print(d[i]) -->print values of dictionary

# Enter size=3
# 1
# 2
# 3
# 4
# 5
# 6
# {1: 2, 3: 4, 5: 6}

# # enter the dictionary and shot it in ascending order

# from ctypes.wintypes import SHORT

# d={}
# x=int(input("eneter size="))
# for i in range(x):
#     k=int(input())
#     v=int(input())
#     d.update({k:v})
# lst=[]
# for i in d:
#     lst.append(d[i])
# print(lst)
# lst.sort()
# print(lst)    

# creat dict check key is present in dict or not
# d={1:2,3:4,5:5,7:9}
# k=int(input("enter key to check="))
# lst=[]
# lst=d.keys()

# print(lst)  
# f=0
# for i in lst:
#     if k==i:
#         print("Present ")  
#         f=1
#         break;
# if f==0:
#     print("not present")        

# ----------------or----------
# d={1:2,3:4,5:5,7:9}
# k=int(input("enter key to check="))
# if k in d:
#     print("present")
# else:
#     print("Not present")    


# -----program3

# x=int(input())
# d={}
# for i in range(1,x+1):
#     d.update({i:i*x})
# print(d)   


# 5
# {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}

# #  sum of keys and sum of values
# d={}
# x=int(input("size="))
# for i in range (x):
#       k=int(input())
#       v=int(input())
#       d.update({k:v})
# lst=d.keys()
# print("sum of keys=",sum(lst)) 
# lst1=d.values()
# print("sum of values=",sum(lst1))


# # size=2
# # 1
# # 2
# # 3
# # 4
# # sum of keys= 4
# # sum of values= 6



#----------delet the key if present in the dict


# d={1:2,3:4,5:5,7:9}
# k=int(input("enter key to check and delet="))
# print("before=",d)
# if k in d:
#     print("present")
#     d.pop(k)
# else:
#     print("not present")
# print("after=",d)


# # enter key to check and delet=3
# # before= {1: 2, 3: 4, 5: 5, 7: 9}
# # present
# # after= {1: 2, 5: 5, 7: 9}
  