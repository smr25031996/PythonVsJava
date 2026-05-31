person={
    'name':'Alice',
    'age':27,
    'city':'Yelgaon'

}

person2=dict(name='BOB',age=27,city='BLD')
print(person)
print(person2)

empty={}

empty2=dict()


print(person2['name'])
print (person.get('age'))

if 'name' in person:
    print(person.get('age'))

person['education']='B.E.'
print(person)
person.update({'city':'Luck','phone':96543433})
print(person)

keys=person.keys()
print(keys)
values=person.values()
print(values)
items=person.items()
print(items)



# Dictionary comprehensions
squares={x: x**2 for x in range(10) if x%2==0}
print(squares)

dict1={'a':1,'b':2,'c':3}
dict2={'d':4,'e':5,'c':8}

merged=dict1 | dict2
print(merged)


#Advanced Dictionary Operations:

from collections import defaultdict, Counter

word_count=defaultdict(int)
text="Hello world hello world"
for  word in text.split():
    word_count[word]+=1

print(word_count)

grouped=defaultdict(list)

for i in range (10):
    grouped[i%3].append(i)

print(grouped)


fruits=['apple','banana','mango','mango','mango','pineapple','grapes','orange']
total=0
print(len(fruits))
for fruit in fruits:
    total+=1

print(total)

fruits_counter=Counter(fruits)
print(fruits_counter)

print(fruits_counter.most_common(2))
