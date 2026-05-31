from out.production.PythonVsJava.Collections import student
from out.production.practice.p1 import unique_numbers

numbers=[1,2,3,4,5,6,7,8,9]
print(numbers)

reversed_numbers=reversed(numbers)

print("reversed number are",reversed_numbers)

reversed_list = numbers[::-1]
print(reversed_list)


numbers = [10, 20, 30, 40]

reversed_list = []

for item in numbers:
    reversed_list = [item] + reversed_list

print(reversed_list)

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_list=list(set(numbers))
print(unique_list)

unique=[]

for item in  numbers:
    if item not in  unique:
        unique.append(item)

print (unique)


numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for item in numbers:
    if item in  frequency:
        frequency[item]+=1
    else:
        frequency[item]=1

print(frequency)



#4. Sort Dictionary by Values


#items() converts dictionary into  tuples

numbers.pop()
print(numbers)
