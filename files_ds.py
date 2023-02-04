
# Open a file

myFile_ds = open('myfile_ds.txt', 'w')

# Get some info
print('Name: ', myFile_ds.name)
print('Is Closed: ', myFile_ds.closed)
print('Opening Mode: ', myFile_ds.mode)

# Write to file
myFile_ds.write('I Love Python')
myFile_ds.write(' and Java')
myFile.close()

# Append to file
myFile_ds = open('myfile_ds.txt', 'a')
myFile_ds.write(' I also like PHP')
myFile.close()

# Read from file
myFile_ds = open('myfile_ds.txt', 'r+')
text_ds = myFile_ds.read(100)

print(text_ds)
