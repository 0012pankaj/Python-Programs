#1. 	Program to print two different strings “Hello” and “World” in different lines.
# print("hello")
# print("world")

#2.Program to print two different strings “Hello” and “World” in a single line.
# print("hello world")

#3.Program to add two entered integer values.
# a=1
# b=2
# print(a+b)

#4. 	Program to subtract two entered integer values.

# a=1
# b=2
# print(b-a)

#Program to multiply two entered integer values.
# print(2*4)
# a=4
# b=2
# print(b*a)

 	#6 Program to input two integer values and calculate first number raised to the power second
	# number.
# a=int(input("a="))
# b=int(input("b="))
# print(a**b)

# 7. 	Program to find the area and perimeter of a rectangle, when the required input (Length and
	# Breadth) are entered by the user.
# length=int(input("length="))
# breath=int(input("breath="))
# print("area of rectangle=",length*breath)    
# print("peremiter  of rectangle=",2*(length+breath))

# 8. 	Program to find the area and circumference of a circle, when the radius is entered by the user.
# 	However, the user can input radius in integer or float.

# radius=int(input("radius="))
# print("area of circle=",3.14*radius*radius)
# print("peremiter of circle=",2*3.14*radius)

# radius=int(input("radius="))
# print("area of circle=%d"%(3.14*radius*radius))
# print("peremiter of circle=%d"%(2*3.14*radius))

# 9. 	Program to find the hypotenuse of a right angled triangle, when the base and height are entered
# 	by the user.

# base=int(input("base="))
# height=int(input("height="))
# print("hypotenus of right triangle=",base**2+height**2) 

# 10. 	Program to input two numbers and print the swapped values of them.
# a=int(input("a="))
# b=int(input("b="))
# c=a+b
# a=c-a
# b=c-b
# print("a=",a)
# print("b=",b)
# print(f'a: {a} b: {b}')

# 11. Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),
# 	when the total number of currency notes counted altogether is minimum and there must be at
# 	least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user.

# rupees=int(input("enter rupees for widrow="))
# rupees=rupees-100

# t=rupees//2000
# rupees=rupees%2000
# f=rupees//500
# rupees=rupees%500
# h=rupees//100
# rupees=rupees%100
# print(f'2000={t} 500={f} 100={h+1} total={t+h+f+1}')

# Program to find the Simple Interest and the total amount when the Principal, Rate of Interest
# 	and Time are entered by the user.

# p=int(input("principle="))
# r=int(input("rate of intrest="))
# t=int(input("time in year="))
# si=(p*r*t)//100
# print("Simple Interest =",si)
# print("tatal amount=",p+si)

# 14. Program to find the Compound Interest compounded annually and the total amount when the
# 	Principal, Rate of Interest and Time are entered by the user.


# p=int(input("principle="))
# r=float(input("rate of intrest="))
# t=int(input("time in year="))
# A=p*((1+(r/100))**t)
# ci=A-p
# print("compund  Interest =",ci)
# print("tatal amount=",int(p+ci))

# . Program that calculates the number of rectangular tiles required to cover a rectangular floor if
# 	the dimensions of the floor and the dimensions of a tile are entered by the user.


# L=int(input("enter length of area="))
# B=int(input("enter breath of area="))
# l=int(input("enter length of tile="))
# b=int(input("enter breath of tile="))
# A=L*B
# a=l*b
# print("the number of rectangular tiles required to cover a rectangular floor ",A//a)

#16 Program to input the number of overs in a Cricket match and output the maximum runs a
# 	player can score in the match. Assume that there are no extra runs or NO balls in the match
# 	played. For example, in a 50 over match, the maximum runs scored are 1653.

# over=int(input("enter the no. of over="))
# print(f"runs in {over} over ={((over-1)*33)+36}")
# for i in range(1, 10, 2):
#  print((i, i * i, i * i * i),end='')
# for i in 'Leopard' :
#  print(chr(ord(i)-32),end='')
# for animal in ['Cat', 'Dog', 'Tiger', 'Lion', 'Leopard'] :
#  print(animal)
# lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
# for i, ele in enumerate(lst) :
#  print(i, ele)
# lst1 = [10, 20, 30, 40, 50]
# lst2 = [ ] # empty list
# lst2 = lst2 + lst1 # lst1, lst2 refer to different lists
# print(lst1)
# print(lst2)
# reverse list
# lst = [10, 2, 0, 50, 4]
# print(lst[::-1]) 



# to take input in list 
# x=int(input())
# lst=[]
# for i in range(x):
# 	lst.append(int(input()))
# for i in lst: 
#   print(i,end=" ")

# x=int(input())
# lst=[]
# for i in range(x):
# 	lst.append(int(input()))

# print(lst[:3])

# lst=[1,2,3,4]
# lst.remove(3)
# print(lst)



# #list que shoping list
# x=int(input())
# lst=[]
# for i in range(x):
# 	lst.append((input()))
# for i in lst: 
#   print(i,end=" ")
# print("enter string")
# st=input()

# x=[1,2,3,4]

# print(x*2)
# names = ['Amir', 'Bear', 'Charlton', 'Daman']
# print(names[-1][-1])


# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
# names2[0] = 'Alice'
# names3[1] = 'Bob'
# sum = 0
# for ls in (names1, names2, names3):
#  if ls[0] == 'Alice':
#   sum += 1
# if ls[1] == 'Bob':
#  sum += 10

# print (sum)


# list1 = [0.5 * x for x in range(0, 4)]
# print(list1)

# list1 = [11, 2,1]
# list2 = [11, 2, 2]
# print(list1 < list2) 

# lst=[1,2,3,4,5]
# # print(list.reverse(lst))
# print(list("a#b#c#d".split('#')))

# myList = [1, 5, 5, 5, 5, 1]
# max = myList[0]
# indexOfMax = 0
# for i in range(1, len(myList)):
#  if myList[i] > max:
#   max = myList[i]
#   indexOfMax = i

# print(indexOfMax)  

# myList = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#  myList[i - 1] = myList[i]

# for i in range(0, 6):
#  print(myList[i], end = " ")

# list1 = [1, 3]
# list2 = list1
# list2[0] = 4
# print(list1)

# def f(values):
#  values[0] = 44
# v = [1, 2, 3]
# f(v)
# print(v)
# x=('hello'+'1'+'2'+'3')
# print(x)

# print('D', end = ' ')
# print('C', end = '')
# print('B'  )
# # print('A')

# print(format("Welcome", "10s"), end = '#')
# print(format(111, "4d"), end = '#')
# print(format(924.656, "3.2f"))

# s="pankaj"
# print(s.__(3))

# t=(1,2,4,3)
# print(t[-1])
# t = (1, 2, 4, 3, 8, 9)
# z=[t[i] for i in range(0, len(t), 2)]
# print (z)
