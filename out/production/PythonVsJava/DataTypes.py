#data types
"""
Numeric Types
Text Types
Boolean Types
"""
#💡 In Python, you do not specify types explicitly! Although, you can have type hints.

#Python is dynamically-typed
#Unlike Java, you can re-assign values of different types to the same variable as you wish. **

x=122334
x="horse"
x=True

#Numeric Types 1/4
#There are only exist the three numeric types float / int / complex in Python.

"""
float types in Python ➡ are equal to double types in Java *
There are NO short / int / long / "float" / double types in Python
"""

my_int=5
my_float=3.141
my_complex=1+2j

# there are also some useful ways to write numbers
speed_of_light=299_792_458
us_national_debt=28.9e+12
ascii_symbol=0x3f
input_bitmask=0b1011_1001





# Integers in Python allow computations beyond usual integer limits without loss of precision.

lightyear_to_meter = 9_460_730_472_580_800
min_milky_way_diameter = 170_000 * lightyear_to_meter

min_milky_way_diameter_plus_one = min_milky_way_diameter + 1

print("Woooooow, the milky way is at least", min_milky_way_diameter, "meters in diameter!")
print("Adding one meter on that, we are at", min_milky_way_diameter_plus_one, "meters.")

# > Woooooow, the milky way is at least 1608324180338736000000 meters in diameter!
# > Adding one meter on that, we are at 1608324180338736000001 meters.



#Numeric Types 3/4: Mathematical Expressions

x=10.5
y=-3

print("x + y = ",x+y)
print("x - y = ",x-y)
print("x / y = ",x/y) #normal
print("x // y = ",x//y)#integer
print("x % y = ",x%y)#integer


print("abs(y) =", abs(y))
print("int(x) =", int(x))
print("float(y ) =", float(y))
print("complex(x,y) = ",complex(x,y))

print("pow(x, 3) =", pow(x, 3))          # exponentiation
print("x ** 3 =", x ** 3)                # exponentiation (alternative syntax)




#Numeric Types 4/4: Mathematical Functions
import math
print(int(math.sqrt(16)))

print(math.factorial(6))
print(math.log(math.e))
print(math.sin(math.pi/2))


