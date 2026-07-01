##problem 1##
##You are given an integer n. You need to return the number of digits in the number.The number will have no leading zeroes, except when the number is 0 itself.
'''
n = int(input ("Enter a number:"))
count = 0
while n > 0:
    count += 1
    n = n//10
print(count)
'''

##problem 2##
##You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
'''
n = int(input("Enter a number:"))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev*10+digit
    n = n // 10
print(rev)
'''
##problem 3##
##You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
## A palindrome number is a number which reads the same both left to right and right to left.
'''
n = int(input("enter a number:"))
rev = 0
original = n
while n > 0:
    digit = n % 10      # Get last digit
    rev = rev*10+digit  # Reverse the number
    n = n // 10         # Remove last digit
print(rev)
if original == rev:
    print(True)
else:
    print(False)
##Time Complexity: O(log n)   Space Complexity: O(1)##
'''
##problem 4##
##You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
##The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.##
'''
n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
if n1 < n2:
    limit = n1              #limit = min(n1, n2)
else:
    limit = n2
gcd = 1
for i in range(1,limit+1):
   if n1 % i == 0 and n2 % i == 0:
    gcd = i
print("GCD :", gcd)
'''
##Time Complexity: O(min(n1, n2))     Space Complexity: O(1)##
