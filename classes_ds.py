# Create class
class User_ds:
  # Constructor
  def __init__(self_ds, name_ds, email_ds, age_ds):
    self_ds.name = name_ds
    self_ds.email = email_ds
    self_ds.age = age_ds
    
  def greeting_ds(self_ds):
    return f'My name is {self_ds.name} and I am {self_ds.age}'
  
  def has_birthday_ds(self_ds):
    self_ds.age += 1
    
    
# Extend class
class Customer(User_ds):
  
 def __init__(self_ds, name_ds, email_ds, age_ds):
    self_ds.name = name_ds
    self_ds.email = email_ds
    self_ds.age = age_ds
    self_ds.balance = 0
    
 def set_balance(self_ds, balance_ds):
    self_ds.balance = balance_ds
    
 def greeting_ds(self_ds):
    return f'My name is {self_ds.name} and I am {self_ds.age} and my balance is {self_ds.balance}'
  
# Init user object
dilara = User_ds('Dilara Samancı', 'dilara@gmail.com', 22)

#print(type(dilara))

print(dilara.name)

print(dilara.age)

print(dilara.email)

print(dilara.has_birthday_ds())

dilara.greeting()

# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com' 25)

janet.set_balance(500)
print(janet.greeting())
