# Function in python:-

def sum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 + num2
    print(f"the sum of {num1} and {num2} is: {sum}")


# sum();

def printName(name):
    print(name)

# printName("Harsh")


# recursion in python:-

def factorial(n): 
    if( n==1 or n == 0):
        return 1
    return n* factorial(n - 1);

fac = factorial(5)
print("Factorial of 5 is: ",fac)

