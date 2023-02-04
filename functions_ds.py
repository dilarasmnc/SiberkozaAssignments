# Create function
def sayHello(name_ds):
  print(f'Hello {name_ds}')
  
  
sayHello('Dilara Samancı')

# Create function
def  sayHello(name_ds = 'Dilara'):
  print(f'Hello {name_ds}')

sayHello()

# Return values
def getSum(num1_ds, num2_ds):
  total = num1_ds + num2_ds 
  return total

print(getSum(3, 4))

# Return values
def getSum(num1_ds, num2_ds):
  total = num1_ds + num2_ds 
  return total

num_ds = getSum(3, 4)

print(num_ds)

# Lambda function 

getSum = lambda num1_ds, num2_ds : num1_ds + num2_ds

print(getSum(10, 3))
