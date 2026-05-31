from out.production.practice.dict import word

text = "Hello, World!"
text1='hi me'

print(text)
print(len(text))

print(text[8])

print(text[7:12])

print(text.lower())
print(text.upper())

text.replace('World', 'Python')  # 'Hello, Python!'
print('text',text.replace('World', 'Python'))

words=text.split()
print(words)
words=text.split(',')
print(words)

print('_'.join(['a','b','c']))
word_with_spacings=" Hello World! "
print(word_with_spacings.strip())
print(word_with_spacings.lstrip())
print(word_with_spacings.rstrip())


# Checking conditions
print(text.startswith('Hello'))
print(text.endswith('!o'))
print(text.isalpha())
print(text.isalnum())
print('abc123'.isalnum())
print('123456'.isdigit())

# Formatting
name="shubham"
age=30
print(f"age:{age}")
print(f"name:{name}")
print("Name:{},Age:{}".format(name,age))
