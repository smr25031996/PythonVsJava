from out.production.PythonVsJava.Collections import squares

fruits=['apple','banana','mango']
numbers=[1,2,3,4,6,6,7]
mixed_list=[1,2,3,'hello']
empty=[]

print (fruits[0])
fruits.append('sapota')
print (fruits)
fruits.insert(0,'peach')
print (fruits)

fruits.remove('apple')
print (fruits)
popped_fruits=fruits.pop(2)
print(popped_fruits)
print(fruits)


numbers.extend([1,1,14])
print(numbers)

numbers.append(77)
print(numbers)

numbers.remove(1)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.count(1)
)
print(numbers)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)

copy_list=numbers.copy()
print(copy_list)

copy_list=numbers[1:4]
print('cp',copy_list)

#List Comprehensions:

square=[x*x for x in  range(10)]
print(square)

squares=[x**3 for x in range (10)]
print(squares)

even_numbers=[num for num in range(25) if num%2==0]
print(even_numbers)

odd_numbers=[odd for odd in  range (25) if  odd%2!=0]
print(odd_numbers)

matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

print(squares.index(27)
      )