#Questions:
#get the length of these list, print the position of each item and print the last item of the list
#print out the data type of each item in the list as well
#append the following items 

single = ['unit']

complex = [{}, None, 'values', 1, 4, 48]  
#append 34
#343 
#'age'

compound  = [1, 43, 4590, 'key', 'value', 'pair', single] #append ['new', 'list']

common_ = ['unit', 'single', 'item'] 
#append {'key','value'}
    
#Answers
single = 'unit'
single_length = len(single)
print(single_length)

#print the position of each item
print(single[0:4])


#print the last item of the list
print(single[-1])

#print data type
print(type(single))


#Answers
complex = [{}, None, 'values', 1, 4, 48]  
data = [34,343,'age']
complex.append(data)
com = len(complex)
print(com)

#print the position of each item
print(complex[0:7])
#print the last item of the list
print(complex[6])

#print out each data types



#Answers
compound  = [1, 43, 4590, 'key', 'value', 'pair', single] #append ['new', 'list']
items = ['new', 'list']
compound.append(items)
comp = len(compound)
print(comp)

#print the position of each item
print(compound[0:8])

#print the last item of the list
print(compound[-1])

#print out each data type
print(type(compound[0]))
print(type(compound[3]))
     

#Answers
common_ = ['unit', 'single', 'item'] 
#append {'key','value'}   

val = {'key','value'}
common_.append(val)
comm = len(common_)
print(comm)

#print the position of each item
print(common_[0:5])

#print the last item of the list
print(common_[-1])

#print out each data types
print(type(common_[0]))

      
#Task 
pos = int(input('Enter a number: '))
while pos > 0 
  print('Positive')



single = ['unit']

complex = [{}, None, 'values', 1, 4, 48]  
#append 34
#343 
#'age'

compound  = [1, 43, 4590, 'key', 'value', 'pair', single] #append ['new', 'list']

common_ = ['unit', 'single', 'item'] 
#append {'key','value'}


#Algorithm for the code

# Get the length of each list
single_length = len(single)
complex_length = len(complex)
compound_length = len(compound)
common_length = len(common_)

# Print the position of each item in the list
for i, item in enumerate(single):
  print(f"Index: {i}, Item: {item}")
for i, item in enumerate(complex):
  print(f"Index: {i}, Item: {item}")
for i, item in enumerate(compound):
  print(f"Index: {i}, Item: {item}")
for i, item in enumerate(common_):
  print(f"Index: {i}, Item: {item}")

# Append new items to the lists
complex.append(34)
complex.append(343)
complex.append('age')
compound.append(['new', 'list'])
common_.append({'key': 'value'})


# Print the last item in the list
single_last = single[-1]
complex_last = complex[-1]
compound_last = compound[-1]
common_last = common_[-1]

# Print the data type of each item in the list
for item in single:
  print(type(item))
for item in complex:
  print(type(item))
for item in compound:
  print(type(item))
for item in common_:
  print(type(item))

# Append new items to the lists
complex.append(34)
complex.append(343)
complex.append('age')
compound.append(['new', 'list'])
common_.append({'key': 'value'})
#Appended Value
single = ['unit']
complex = [{}, None, 'values', 1, 4, 48]  
complex.append(34)
complex.append(343)
complex.append('age')
compound = [1, 43, 4590, 'key', 'value', 'pair', single]
compound.append(['new', 'list'])
common_ = ['unit', 'single', 'item']
common_.append({'key': 'value'})

# Get the length of each list
single_length = len(single)
complex_length = len(complex)
compound_length = len(compound)
common_length = len(common_)

# Print the position of each item in the list
for i, item in enumerate(single):
  print(f"Index: {i}, Item: {item}")
for i, item in enumerate(complex):
  print(f"Index: {i}, Item: {item}")
for i, item in enumerate(compound):
  print(f"Index: {i}, Item: {item}")
for i, item in enumerate(common_):
  print(f"Index: {i}, Item: {item}")

# Print the last item in the list
single_last = single[-1]
complex_last = complex[-1]
compound_last = compound[-1]
common_last = common_[-1]

# Print the data type of each item in the list
for item in single:
  print(type(item))
for item in complex:
  print(type(item))
for item in compound:

#List
'''
list_type = ['STRING', 1, 3, {'fruit':'apple'}]

print('length of old list:',   len(list_type), 
      '\nold list content:',  list_type)

list_type.append('another string')

#print('\nlist length:', len(list_type),
#      '\nlist content:',   list_type)


#len of a list
list_length = len(list_type)

index_of_string =list_type.index({'fruit':'apple'})
#print('position of dictionary:',index_of_string)
'''

#permutation

#BE

#BE 1st
#EB 2nd


# cup question

#cup 1st
#cpu 2nd

#upc 3rd
#ucp 4th

#puc 5th
#pcu 6th

#factoria !

#permutate_BE = 2! = 2 * 1
#= 2
#permutate_cup = 3! = 3  * 2  * 1
#= 6

file1, file2, file3, file4

ext1, ext2, ext3, ext4
#four files map/match with 4 extension
#outcome  = 4 * 4 = 16
file1+ext1
file1+ext2
file1+ext3
file1+ext4

file2+ext1
file2+ext2
...



