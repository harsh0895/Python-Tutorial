# intro to dictionary:-

marks = {
    "harry": 50,
    "harsh": 40
}

print(marks)
print(type(marks))

print(marks["harry"])
print(marks["harsh"])

print(marks.keys())
print(marks.items())
print(marks.values())

marks.update({"harry": 99})
print(marks)

marks.get("harry")
marks["harry"]
print(marks)