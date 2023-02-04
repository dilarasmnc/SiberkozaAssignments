
x_ds = 10
y_ds = 50

# Comparison Operators (==, !=, >, <, >=, <=) 

# Simple if
if x_ds > y_ds:
  print(f'{x_ds} is greather than {y_ds}')

# If/ Else conditions 
if x_ds > y_ds:
  print(f'{x_ds} is greather than {y_ds}')
else:
  print(f'{y_ds} is greather than {x_ds}')

# elif
if x_ds > y_ds:
  print(f'{x_ds} is greather than {y_ds}')
elif x_ds == y_ds:
  print(f'{x_ds} is equal to {y_ds}')
else:
  print(f'{y_ds} is greather than {x_ds}')

# Nested if
if  x_ds > 2:
  if  x_ds <= 10:
    print(f'{x_ds} is greather than 2 and less than or equal to 10')
  
# Logical operators (and, or, not) 

# and
if  x_ds > 2 and x <= 10:
     print(f'{x_ds} is greather than 2 and less than or equal to 10')
# or
if  x_ds > 2 or x <= 10:
     print(f'{x_ds} is greather than 2 or less than or equal to 10')

# not
if not(x_ds == y_ds):
  print(f'{x_ds} is not equal to {y_ds}')

# Membership Operators (in, not in) 

numbers_ds = [1,2,3,4,5]

# in
if x_ds in numbers_ds:
  print(x_ds in numbers_ds)

# not in 
if x_ds not in numbers_ds:
  print(x_ds not in numbers_ds)

# Identity Operators (is, is not) 

# is 
if x_ds is y_ds:
  print(x_ds is y_ds)

# is not 
if x_ds is not y_ds:
  print(x_ds is not y_ds)
  
  
