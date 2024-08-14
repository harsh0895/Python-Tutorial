# Function in python:-


# slicing in list:-

# li = [1,2,3,4,45]
# print(li)
# print(li[0])
# print(li[0:2])
# print(li[: 4])
# print(li[-3: -1])


# li[1:2] = ['harsh']
# print(li)






def are_strings_balanced(s1, s2):
   
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    # Check if all characters in s1 are in s2
    return set_s1.issubset(set_s2)


s1 = "or"
s2 = "world"

if are_strings_balanced(s1, s2):
    print(f"The strings '{s1}' and '{s2}' are balanced.")
else:
    print(f"The strings '{s1}' and '{s2}' are not balanced.")
