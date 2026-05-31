numbers=[10,20,30,40,50]

reversed_list=numbers[::-1]

print(reversed_list)


#list[start:end:step]

reversed_list=numbers[0:3:-1]
print(reversed_list)

numbers=[10,10,10,10,20,30,40,50]

unique_numbers=list(set(numbers))
print(unique_numbers)

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = []


for  item in numbers:
    if item not in unique_numbers:
        unique_numbers.extend([item])


print (unique_numbers)



numbers = [1, 2, 2, 3, 3, 3, 4]

frequency={}

for item in numbers:
    if item not in frequency:
        frequency[item]=+1
    else:
        frequency[item]=1

print(frequency)

