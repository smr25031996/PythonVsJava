# 🐍 Collections

"""
Lists and arrays in Java ➡ are just list in Python (but, there is also tuple)
Maps in Java ➡ are dict in Python
Sets in Java ➡ are also set in Python
"""
import copy
import pprint

numbers = [1, 2, 3, 4, 5, 6]

names = ["Janie", "ALI", "Alice"]

mixed = [1, 2, "Max", 3.14]

print(names[0])
names[0] = "peter"
print(names[0])

numbers.append(-3)
print(numbers)

names.insert(2, "rambo")

print(names)

names.remove("Alice")
print(names)

del names[0]
print(names)

print(numbers[-1])  # Last element

fruits = ["Apple", "Banana"]

fruits.insert(1, "Orange")
print(fruits)

fruits.extend(["guava", "mango"])

print(fruits)

fruits.pop(-2)
print(fruits)

fruits.clear()
print(fruits)

# List Slicing
numbers = [90, 20, 30, 40, 50, 60]
print(numbers[1:4])

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
print(len(numbers))

print(100 in numbers)

squares = [x * x for x in range(5)]
print(squares)

# tuple

"""
Ordered
Immutable (cannot change)
Allows duplicates
"""
data = (20, 30, 20,20)


print(data)

print(data[1])


print(data.count(20))


print("hi",data.index(20))


#Tuple Packing and Unpacking

student=("shubham",22)
name,age=student
print(name,"and age is ",age)


#3. Set in Python
"""
A Set is:
Unordered
Mutable
No duplicates allowed
"""

nums={1,2,3,4,5,6,7,8,9,2}
print(nums)
nums.add(99)
print(nums)
nums.update([87,78,69,50])
print(nums)

nums.discard(50)
print(nums)


a={1,2,3,4,5,6,7,8,9}
b={2,1,13,4,15,16,17,18,19,20,21,22,23}

print(a|b)
print(a&b)
print(a^b)
print(a-b)


#Dictionary in Python

"""
A Dictionary stores data in:
Key → Value format
Mutable
Ordered (Python 3.7+)"""

student={
    "name":"Shubham",
    "age":21,
    "course":"Python"
}

print(student["name"])
print(student.get("age"))
print(student.get("course"))

print(student.keys())
print(student.values())

print(student.items())

for key,value  in student.items():
    print(key,"->",value)


employees = {
    101:{"name":"LIA","salary":5000},
    102:{"name":"Shubham","salary":7000},

}

students = [
    {"id": 1, "name": "Shubham", "marks": 90},
    {"id": 2, "name": "Rahul", "marks": 85}
]

for student in students:
    print(student["name"], student["marks"])

print(max(nums))
print(min(nums))
print(sum(nums))
print (sorted(nums))

"""
Difference Between Collections

Feature	    List	Tuple	Set	    Dictionary

Ordered	    Yes	    Yes	    No	    Yes

Mutable	    Yes	    No	    Yes	    Yes

Duplicates	Yes	    Yes	    No	    Keys No

Indexing	Yes	    Yes	    No	    By key

"""

z=[1,2]
z.append([3,4])
print(z)

z.extend([5,6])
print(z)

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

print(b)
