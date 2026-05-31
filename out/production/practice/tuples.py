from collections import namedtuple

point=(10,20)

rgb=(255,0,0)
single_tuple=(5,)
empty=()
mixed_tuple=(1,'misxed',3.6)

coordinates=10,20,30

numbers=(1,2,3,4,5,6,7,8,9,10)
def get_min_max(numbers):
    return min(numbers),max(numbers)

print(get_min_max(numbers))


x,y=point
print(x,y)

x,y,z=coordinates
print(x,y,z)
list_from_tuple=list(point)
print(list_from_tuple)
tuple_from_list=tuple(list_from_tuple)
print(tuple_from_list)


Person=namedtuple('Person',['name','age','city'])

alice=Person('Alice',30,'New York')
print(alice.name)
print(alice.age)
print(alice.city)
