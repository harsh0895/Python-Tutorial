# que 1:- Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("enter your age: "))

if( age < 13 ):
    print("You are child")
elif( age >= 13 and age <= 19 ):
    print("You are Teenager")
elif( age >= 20 and age <=59 ):
    print("You are Adult")
else:
    print("You are Senior")

# que 2:- Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

ticket_price = 12 if age >= 18 else 8
day = 'wed'

if(  day == 'wed' ):
    ticket_price = ticket_price - 2
    print(f"price for adults {ticket_price}")
else:
    print(f"price for adults {ticket_price}") # id day is not wednesday...

# que 3:- Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

sub1 = int(input("enter marks for suject one: "))
sub2 = int(input("enter marks for suject two: "))
sub3 = int(input("enter marks for suject three: "))

total = sub1 + sub2 + sub3
result = total/3

if( result >= 90 and result <= 100 ):
    print('A')
elif( result >= 80 and result < 89 ):
    print('B')
elif( result >= 70 and result < 79 ):
    print('C')
elif( result >= 60 and result < 69 ):
    print('D')
elif( result < 60 ):
    print('Fail')

# que 4:- Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe).

fruit = "Banana"
color = "green"

if( fruit == "Banana"):
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")

