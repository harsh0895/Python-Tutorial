# List in python:-

friends = [ 1,2,3,4,5,6,"Harsh", False, True ];

# print(friends[0])

# friends[0] = "kjdfldfsl"

 
# for item in friends:
#     print(item)

# i = 0
# while( i < len(friends)):
#     print(friends[i])
#     i = i + 1

tea = ["black", "green", "Oolang", "white"]
print(tea)

# tea[1:2] = "harsh" # --> ["black", 'h', 'a', 'r', 's', 'h', "Oolang", "white"] 
# print(tea)
tea[1:2] = ["harsh"] # --> ["black", "harsh", "Oolang", "white"] 
print(tea)

tea[1:3] = ["harsh", "aman"]
print(tea)

for teas in tea:
    print(teas, end=" ")