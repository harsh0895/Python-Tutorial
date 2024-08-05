# string functions in python:-


firstName = "Harsh bhola"
digit = '12345678'

print(firstName)

print(len(firstName))
print(firstName.upper()) # it will convert all the characters of the string into the uppercase!
print(firstName.lower())  # it will convert all the characters of the string into the lowercase!
print(firstName.swapcase()) # it converts all the uppercase character into the lowercase and lowercase into the uppercaser (HArsh --> haRSH)!

print(firstName.endswith('rsh'))
print(firstName.startswith('Ha'))
print(firstName.capitalize()) # it will capitalize only first character of the string (harsh --> Harsh)!
print(firstName.title()) # it converts the first character of each word to the string! (harsh bhola --> Harsh Bhola)!
print(firstName.count('a')) # it check the occurrence of the particular chacacter in the string!
print(digit.isdigit()) # it checks the given string is digit or not!
print(firstName.split()) # it will convert string into the list!
print("".join(firstName)) # it will convert list into the one string!
print(firstName.find('h')) # it check the gievn character exists in the given string or if not exists than it return -1!


s = "hello world"
print(s)
print(s.replace("world", "Python"))  # Output: "hello Python"
space = "   hello   "
print(space)
print(space.strip())  # Output: "hello"

chai_type = "masala"
quantity = 2
order = "I ordered {} cups of {} chai"

print(order.format(quantity, chai_type))
print(f"i ordered {quantity} cups of {chai_type}")

chai_variety = ["lemlon", "masala", "ginger"]
 

# Important note:- after applying all these function on the string which is firstName won't be change because strings are imutable in python!

