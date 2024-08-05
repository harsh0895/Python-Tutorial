# que 1 :-  Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# count = 0
# for item in numbers:
#     if item > 0:
#         count = count + 1
#     else:
#         continue

# print(f"{count} numbers are positive in the given list")

# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

# sum = 0
# for item in numbers:
#     if item % 2 == 0:
#         sum = sum + item
    
# print(f"The sum of even numbers is: {sum}")

# 3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# num = int(input("enter your table number: "))

# for i in range(1, 11):
#     if( i == 5 ):
#         continue
#     else:
#         print(f"{num} X {i} = {num * i}")
        

# 4. Reverse a String
# Problem: Reverse a string using a loop.

name = "Harsh"

c = ''
for s in name:
    c = c + s
    
print(c)

# 5. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

fac = 5
factorial = 1
i = 1

while( i <= fac):
    factorial = factorial * i
    i = i + 1

print(f"Factorial of {fac} is {factorial}")

# que 6:- Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()
for item in items:
    if item in unique_items:
        print(f"duplicate item is {item}")
        break
    else:
        unique_items.add(item)

