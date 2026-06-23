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
match day:
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