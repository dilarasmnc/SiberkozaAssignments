# Create list
numbers_ds = [1, 2, 3, 4, 5]
fruits_ds = ['Apples', 'Oranges', 'Grapes', 'Pears']
             
# Use a constructor
numbers2_ds = list((1, 2, 3, 4, 5))

print(numbers_ds, numbers2_ds)

# Get a value
print(fruits_ds[1])

# Get length
print(len(fruits_ds))

# Append to list
fruits_ds.append('Mangos')

print(fruits_ds)

# Remove from list
fruits_ds.remove('Grapes')

print(fruits_ds)

# Insert into position
fruits_ds.insert(2, 'Strawberries')

print(fruits_ds)

# Remove with pop
fruits_ds.pop(2)

print(fruits_ds)

# Reverse list
fruits_ds.reverse()

print(fruits_ds)

# Sort list 
fruits_ds.sort()

print(fruits_ds)

# Reverse sort
fruits_ds.sort(reverse=True)

print(fruits_ds)

# Change value
fruits_ds[0] = 'Blueberries'

print(fruits_ds)

