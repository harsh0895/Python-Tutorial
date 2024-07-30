# Que1:- Write a program to find the greatest number entered by the user?

# n1 = int(input("enter first number: "))
# n2 = int(input("enter second number: "))
# n3 = int(input("enter third number: "))
# n4 = int(input("enter fourth number: "))

# if( n1 > n2 and n1 > n3 and n1 > n4 ):
#     print("first number is greater!")
# elif( n2 > n1 and n2 > n3 and n2 > n4 ):
#     print("second number is greater!")
# elif( n3 > n1 and n3 > n2 and n3 > n4 ):
#     print("Third number is greater!")
# else:
#     print("Fourth number is greater!")


# Que2:- Write a program to check the given comment is spam or not?

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

msg = input("enter your comment: ")

if( (p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg) ):
    print("Your comment is spam...")
else:
    print("Your comment is not a spam...")


