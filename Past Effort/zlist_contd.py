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

#Task 
#get the length of these list,append the attached values print the position of each item and print the last item of the list
#print out the data type of each item in the list as well

#Questions:
single = 'unit'

complex = [{}, None, 'values', 1, 4, 48]  
#append 34
#343 
#'age'

compound  = [1, 43, 4590, 'key', 'value', 'pair', single ] #append ['new', 'list']

common_ = ['unit', 'single', 'item'] 
#append {'key','value'}


#appended items
complex = [{}, None, 'values', 1, 4, 48]  
complex.append(34)
complex.append(343)
complex.append('age')

compound = [1, 43, 4590, 'key', 'value', 'pair', single] #append ['new', 'list']
compound.append(['new', 'list'])
compound = [1, 43, 4590, 'key', 'value', 'pair', 'unit',['new','list'] ]
                                                         
common_ = ['unit', 'single', 'item'] 
#append {'key','value'}
common_.append({'key','value'})

list_created_with_variables =  [complex, common_, compound, single]


#get the length of the list
length_of_single = len(single)
print("The length of single value is:",length_of_single)
length_of_complex = len(complex)
print("The length of complex value is:",length_of_complex)
length_of_compound = len(compound)
print("The length of compound value is:",length_of_compound)
length_of_common_ = len(common_)
print("The length of common_ value is:", length_of_common_)


#print the position of each item
print(single.index('unit'))

for content in enumerate(compound):
      print("Position_of_compound_values:",content)
for val in enumerate(complex):
     print("Position_of_complex_values",val)

for things in enumerate(common_):
  print("Position_of_common_value", things)


#print the last item of the list
print("single last value is:",single[-1])
print("complex last value is:",complex[-1])
print("compound last value is:",compound[-1])
print("common_ last value is:",common_[-1]
)

#print out the data type of each item in the list as well
print(type(single))
for itemx in compound:
  data = type(itemx)
  print(data)
for itemz in complex:
  stuff = type(itemz)
  print(stuff)
for items in common_:
  load = type(items)
  print(load) 