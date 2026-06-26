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