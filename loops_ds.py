# for loop

people_ds = ['Jhon', 'Paul', 'Sara', 'Susan']

# Simple for loop
 for person_ds in people_ds:
   print(f'Current Person: {person_ds}')
  
# Break
 for person_ds in people_ds:
    if person_ds == 'Sara':
      break
   print(f'Current Person: {person_ds}')
  
# Continue
 for person_ds in people_ds:
    if person_ds == 'Sara':
      continue
   print(f'Current Person: {person_ds}')
  
# range
for i_ds in range(len(people_ds)):
  print(people_ds[i_ds])
  
for i_ds range(0, 11):
  print(f'Number: {i_ds}')
  
# while loop

count_ds = 0
while count_ds <= 10:
  print(f'Count: {count_ds}')
  count += 1

  
