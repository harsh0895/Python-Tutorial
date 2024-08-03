# que 1:- Write a Program to print Fibonnaci series in python up to first 15 terms. 
# Fibonacci series 0,1,1,2,3,5,8,13,21,55,89,144

number = int(input('enter your number: '))

firstNum = 0
secondNum = 1

for i in range(1, number+1):
    print(firstNum)
    currentNum = firstNum + secondNum
    firstNum = secondNum
    secondNum = currentNum


# que 2:- Write a program to find the Factorial of a user entered number.

number = int(input('enter your number: '))

factorial = 1;

for i in range(1, number+1):
    factorial = i * factorial

# print(f"the factorial of given number is: {factorial}")


# que 3: Write a program to get the table of a user entered number.

number = int(input('enter your number: '))

for i in range(1, 11):
    print(f"{number} X {i} = {number * i}")



# que 4:  Write a program to generate a random number less than 100 and user entered number and find if the user entered number was greater or smaller or equal.

import random

random_number = random.randint(1, 100)
# print(random_number)

number = int(input('Choose a number between 1 to 100: '))


if( random_number < number ):
    print('Your number is greater!')
elif( random_number == number ):
    print("Your number is equal to the random number entered by the user!")
elif( random_number > number ):
    print("Your number is smaller then random number!")



# que 5: Write a program to find if a year is leap or not.

year = int(input('enter you year: '))

if( year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year!")
else:
    print(f"{year} is not a leap year!")



# que 6: Write a program to get 3 user input numbers and check if the numbers are in ascending or descending or they are neither in 
# ascending nor in descending order.

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

print(n1)
print(n2)
print(n3)

if( n1 < n2 and n2 < n3 ):
    print("numbers in ascending order!")
elif( n1 > n2 and n2 > n3 ):
    print('numbers in descending order!')
else:
    print("number not in ascending or descending!")


# que 7: Write a program to sort a list of 5 numbers.

li = [ 2, 1, 3, 5, 4 ]

li.sort()
print(li)

# que 8: Write a program Get the Largest and smallest number from a list.

l2 = [ 2, 1, 3, 5, 4 ]

largest = l2[0]
smallest = l2[0]

for item in l2:
    if( largest < item ):
        largest = item
    
    if( smallest > item ):
        smallest = item

print(f"largest number is: {largest}")
print(f"smallest number is: {smallest}")\

# by using in-built methods:-
l = max(l2)
m = min(l2)
print(l, m)

