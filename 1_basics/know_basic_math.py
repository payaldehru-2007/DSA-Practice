##problem 1##
##You are given an integer n. You need to return the number of digits in the number.The number will have no leading zeroes, except when the number is 0 itself.

n = int(input ("Enter a number:"))
count = 0
while n > 0:
    count += 1
    n = n//10
print(count)
