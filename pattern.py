# n=int(input())
# for i in range(n):
#     print("* "*i)
#     print()

# 
# *

# * *

# * * *

# * * * *

# * * * * *
n=int(input())
for i in range(n):
    print("* "*n)
    n-=1
    print()

# * * * * * 

# * * * *

# * * *

# * *

# *

# n=int(input())
# sp=n+1
# for i in range(n+1):
#     print("  "*sp,"*   "*i)
#     sp-=1
#     print()

#          *

#        *   *

#      *   *   *

#    *   *   *   *

#  *   *   *   *   *

# row=14
# print("*"*row, end="\n")
# i=(row//2)-1
# j=2
# while(i!=0):
#     print("*"*i,end='')
#     print(" "*j,end='')
#     print("*"*i,end='\n')
#     i-=1
#     j+=2
# **************
# ******  ******
# *****    *****
# ****      ****
# ***        ***
# **          **
# *            *

# n=int(input())
# print("*"*2*(n+1),end="\n")
# for i in range(n):
#     for j in range(i,n):
#         print("*",end="")
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(" ",end="") 
#     for j in range(i,n):
#         print("*",end="")   
#     print()


    
# # ****************
# # *******  *******
# # ******    ******
# # *****      *****
# # ****        ****
# # ***          ***
# # **            **
# # *              *


# n=int(input())

# for i in range(n):
#     for j in range(i,n):
#         print("  ",end="")
#     for j in range(i):
#         print("* ",end="")
#     for j in range(i+1):
#         print("* ",end="") 
#     for j in range(i,n):
#         print("  ",end="")   
#     print()
#                 *
#               * * *
#             * * * * *
#           * * * * * * *
#         * * * * * * * * *
#       * * * * * * * * * * *
#     * * * * * * * * * * * * *
#   * * * * * * * * * * * * * * *


# n=int(input())

# for i in range(n-1):
#     for j in range(i,n):
#         print("  ",end="")
#     for j in range(i):
#         print("* ",end="")
#     for j in range(i+1):
#         print("* ",end="") 
#     for j in range(i,n):
#         print("  ",end="")   
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print("  ",end="")
#     for j in range(i,n-1):
#         print("* ",end="")
#     for j in range(i,n):
#         print("* ",end="") 
#     for j in range(i,n):
#         print("  ",end="")   
#     print()

    
#               *
#             * * *
#           * * * * *
#         * * * * * * *
#       * * * * * * * * *
#     * * * * * * * * * * *
#   * * * * * * * * * * * * *
#     * * * * * * * * * * *
#       * * * * * * * * *
#         * * * * * * *
#           * * * * *
#             * * *
#               *

# n=int(input())
# print("*"*n)
# for i in range((n//3)-1):
#     print("*"," "*(n-4),"*")
# print("*"*n)

# 13
# *************
# *           *
# *           *
# *           *
# *************

# n=int(input())
# x=1
# sp=n+1
# for i in range (n):
#     print(" "*sp,"*"*x)
#     x+=2
#     sp-=1
    
#     4
#       *
#      ***
#     *****
#    *******


# n=int(input())
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     for j in range(i+1):
#         print("*",end="")    
#     print()        

#     4
#     *
#    ***
#   *****
#  *******

# n= int(input("=="))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()    
                    
#      *     *
#     **    **
#    ***   ***
#   ****  ****
#  ***** *****