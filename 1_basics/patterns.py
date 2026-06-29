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

##problem 9##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
    * 
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(n-i)-1):
        print("*",end="")
    print()
'''
##problem 10##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
*
**
***
****
*****
****
***
**
*

n = 5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    print()
'''
##problem 11##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1

n = 5
for i in range(n):
    for j in range(i+1):
        print(1 - ((i + j) % 2),end=" ")
    print()
'''

##problem 12##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1        1
12      21
123    321
1234  4321
1234554321

n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    for j in range(2*(n-i-1)):
        print(" ",end="")
    for j in range(i+1):
        print(i+1-j,end="")
    print()
'''

##problem 13##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

n = 5
num = 1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num = num+1
    print()
'''

##problem 14##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
A
AB
ABC
ABCD
ABCDE

n = 5 
for i in range(n):
    for j in range(i+1):
        print((chr(65+j)),end="")
    print()
'''

##problem 15##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
ABCDE
ABCD
ABC
AB
A

n = 5 
for i in range(n):
    for j in range(n-i):
        print((chr(65+j)),end="")
    print()
'''

##problem 16##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
A
BB
CCC
DDDD
EEEEE

n = 5 
for i in range(n):
    for j in range(i+1):
        print((chr(65+i)),end="")
    print()
'''
##problem 17##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

n = 5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    ch = 65
    for j in range(2*i+1):
        print((chr(ch)),end="")
        if j<i:
            ch = ch+1 ##increase character=a,b,c
        else:
            ch = ch-1 ##decrease character=c,b,a
    print()
'''
##problem 18##
##Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
'''
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5

n = 5
for i in range(n):
    for j in range(i+1):
        print((n-i+j),end=" ")
    print()

E 
D E 
C D E 
B C D E 
A B C D E

n = 5 
for i in range(n):
    for j in range(i+1):
        print(chr(65+(n-1-i)+j),end=" ")
    print()

'''