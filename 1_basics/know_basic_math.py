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
class Solution:
    def isPalindrome(self, n):
        dup = n
        revNum = 0
        while n>0:
            lastdigit = n%10
            n = n//10
            revNum = (revNum*10)+lastdigit
        if dup == revNum :
            return True
        else:
            return False