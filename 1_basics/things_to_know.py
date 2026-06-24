##strivers A2Z DSA Sheet

##problem 1 ##
##Complete the function printNumber which takes an integer input from the user and prints it on the screen.
'''
a = int(input("enter a number :"))
print(a)
'''

##problem 2##
##Given marks of a student, print on the screen:Grade A if marks >= 90
##Grade B if marks >= 70 Grade C if marks >= 50 Grade D if marks >= 35 Fail, otherwise.
'''
marks = int(input("enter marks:"))
if (marks>=90):
    print("grade A")
elif marks>=70 and marks<90:
   print("grade B")
elif marks>=50 and marks<70:
    print("grade C")
elif marks>=35 and marks<50:
    print("grade D")
else:
    print("fail")
 '''

##problem 3##
##Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
'''
day = int(input("enter the day number :"))

    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case_:
        print("not valid")    
'''

## problem 4##
##Take 5 integers as input from the user and store them in an array (list).Then print:
##The complete array. The first element. The last element. The element at index 2.
'''
arr1 = int(input("Enter the number: "))
arr2 = int(input("Enter the number: "))
arr3 = int(input("Enter the number: "))
arr4 = int(input("Enter the number: "))
arr5 = int(input("Enter the number: "))
arr = [arr1, arr2, arr3, arr4, arr5]
print(arr)
print(arr[0])
print(arr[4])
print(arr[2])
'''

## problem 5##
##Given two integers low and high, return the sum of all integers from low to high inclusive.Input: low = 3, high = 8
'''
sum = 0
for i in range(3,9):
  sum = sum + i
print(sum)
'''

## problem 6##
##Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.
## A number ends with digit 2 if its last digit is 2.
'''
sum = 0
num = 2
i = 0
while i < 50:
    sum = sum + num
    num = num + 10
    i = i +1 

print(sum)
'''

## problem 7##
##Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.Input: n=5, arr = [1,2,3,4,5]
'''
arr = [1,2,3,4,5]
left = 0
right = len(arr)-1
while left<right:
 arr[left] , arr[right] = arr[right] , arr[left]
 left = left+1
 right = right-1
 print(arr)
'''
