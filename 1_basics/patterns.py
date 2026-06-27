## problem 1##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N =5
'''
*****
*****
*****
*****
*****
n =5
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
'''

##problem 2##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
*
**
***
****
*****

n = 5
for i in range(n):
    for j in range(i+1):
        print("*" , end ="")
    print()
'''

##problem 3##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1
12
123
1234
12345

n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1 , end = "")
    print()
'''

## problem 4##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1
22
333
4444
55555

n = 5
for i in range(n):
    for j in range(i+1):
        print(i+1 , end ="")
    print()
'''

##problem 5##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
*****
****
***
**
*

n = 5 
for i in range (n):
    for j in range(n-i):
        print("*" , end="")
    print()
'''
##problem 6##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
12345
1234
123
12
1


i           r           j           o
0           5           0,1,2,3,4   12345
1           4           0,1,2,3     1234
2           3           0,1,2       123
3           2           0,1         12
4           1           0           1


n = 5
for i in range(n):
    for j in range(n-i)
        print(j+1,end ="")
    print()
'''
##problem 7##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
    *
   ***
  *****
 *******
*********

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    
    for j in range(2*i+1):
        print("*",end ="")
    print()
'''

##problem 8##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
*********
 *******
  *****
   ***
    *


n = 5
for i in range(n):
    for j in range(i):
        print(" ",end ="")
    for j in range(2*(n-i)-1):
        print("*",end ="")
    print()
'''