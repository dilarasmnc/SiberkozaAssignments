name_ds = 'Dilara'
age_ds = 22

# Concatenate
print('Hello, my name is ' + name_ds+ ' and I am ' + str(age_ds))


# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name_ds, age=age_ds))

#F-Strings (3.6+)
print(f'Hello, my name is {name_ds} and I am {age_ds}')

# String Methods

s_ds = 'hello world'

# Capitalize string 
print(s_ds.capitalize())

# Make all uppercase
print(s_ds.upper())

# Make all lower
print(s_ds.lower())

# Swap case
print(s_ds.swapcase())

# Get length
print(len(s_ds))

# Replace
print(s_ds.replace('world', 'everyone'))

# Count
sub = 'h'
print(s_ds.count(sub))

# Starts with
print(s_ds.startswith('hello'))

# Ends with
print(s_ds.endswith('d'))

# Split into a list 
print(s_ds.split())

# Find position
print(s_ds.find('d'))

# Is all alphanumeric
print(s_ds.isalnum())

#Is all alphabetic
print(s_ds.isalpha())

# Is all numeric
print(s_ds.isnumeric())

