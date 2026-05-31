#4. Sets (Mutable, Unordered, Unique)
#Sets store unique elements with fast membership testing.
from out.production.practice.p2 import unique

fruits={"apple","banana","mango"}
numbers={1,2,3,4,5,6,7,8,9,"hellow"}
print(numbers)

list_with_dupes = [1, 2, 2, 3, 3, 3, 4]
print(list_with_dupes)
unique_numbers = set(list_with_dupes)
print(unique_numbers)

fruits.add('grape')
fruits.update(['kiwi',"lope"])
fruits.remove('kiwi')
fruits.discard('set')
popped_fruits = fruits.pop()
print(popped_fruits)

# Set operations
set_a={1,2,3,4,5}
set_b={4,5,6,7,8,9}
union=set_a.union(set_b)
print(union)
print(set_a  | set_b)

print(set_a & set_b)

print(set_a - set_b)
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

print({1,2}.issubset(set_a))
print(set_a.issuperset({88,99}))
print(set_a.isdisjoint({1,7}))

#Frozenset (Immutable Set):

fs=frozenset([1,2,3,4,5])
print(fs)

dict_with_frozenset={frozenset([1,2,3]):'value'}
print(dict_with_frozenset)

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
union_fs = fs1 | fs2  # frozenset({1, 2, 3, 4, 5})
print(union_fs)