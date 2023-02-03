# Create dict
person_ds = {
  'first_name_ds': 'Dilara',
  'lats_name_ds': 'Samanci',
  'age_ds': 22
}

print(person_ds, type(person_ds))

# Use constructor
person2_ds = dict(first_name_ds='Sara', last_name_ds='Williams')

print(person2_ds, type(person2_ds))

# Get value
print(person_ds['first_name_ds'])
print(person_ds.get('last_name_ds'))

# Add key/value
person_ds['phone_ds'] = '555-555-5555'

print(person_ds)

# Get dict keys
print(person_ds.keys())

# Get dict items
print(person_ds.items())

# Copy dict
person2_ds = person_ds.copy()
person2_ds['city'] = 'Boston'

print(person2_ds)

# Remove item
del(person_ds['age_ds'])
person_ds.pop('phone_ds')

print(person_ds)

# Clear 
person_ds.clear()

print(person_ds)

# Get length
print(len(person2_ds))

# List of dict
people_ds = [
    {'name_ds': 'Martha', 'age_ds': 30},
    {'name_ds': 'Kevin', 'age_ds': 25}
]

print(people_ds[1]['name_ds'])
