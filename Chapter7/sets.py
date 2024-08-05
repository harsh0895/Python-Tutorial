# introduction of sets in python:- 

setone = { 1, 2, 3, 4, }
print(setone)

settwo = { 1, 3 }
print(settwo)

intersection = setone & settwo
print(intersection)

union = setone | settwo
print(union)

emptySet = set()
print(emptySet)
print(type(emptySet))

minus = setone - settwo
print(minus)

