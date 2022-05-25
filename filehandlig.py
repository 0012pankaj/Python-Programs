#longest word in file
# f=open("abc.txt",'r')
# l= f.read().split()
# long=len(l[0])
# for i in l:
#     if(len(i)>long):
#         long=len(i)
#         st=i
# print(st)
# f.close()

#no of line in a file
# f=open("abc.txt",'r')
# l= f.read().split("\n")
# print(len(l))
# print(l)
# f.close()

#count frequency in a file
# f=open("abc.txt",'r')
# l= f.read().split()
# print(len(l))
# print(l)
# f.close()

#
# with open('abc.txt','r+') as f:
# 	line = f.readlines()
# 	print(line)
# 	[print(l.strip()) for l in line] 

#que 4
import numpy as np
r=int(input())
c=int(input())
l1=[]
for i in  range(r):
    x=int(input())
    if(x%3==0):
        l1.append(x)
    else:
        l1.append(0)
        

l2=[]
for i in  range(c):
    y=int(input())
    if(y%3==0):
        l2.append(y)
    else:
        l2.append(0)
l3=[]
l3.append(l1)
l3.append(l2)
    
# a=np.array(l3,int)
print(np.array(l3,int))


