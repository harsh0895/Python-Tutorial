# method of lists:-
# in the case of strings the original string won't change but in the case of list kikt will be change after applying the methods of lists!



friends = [ 1,2,3,4,5,6,"Harsh", False, True ]

print(friends)
friends.append("Nitin")
print(friends)



l1 = [ 10, 2, 4, 5, 5, 6, 7 ]
l1.sort()
l1.reverse()
l1.insert(5, 100)
l1.pop()
l1.pop(2) # it will delete the 2nd index value from the list!
l1.remove(10) # it removes the value 10 from the list!
print(l1)

maximum = max(l1)
minimum = min(l1)
Sum = sum(l1)

print(maximum)
print(minimum)
print(Sum)
