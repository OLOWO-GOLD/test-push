#List

list_type = ['STRING', 1, 3, {'fruit':'apple'}]

print('length of old list:',   len(list_type), 
      '\nold list content:',  list_type)

list_type.append('another string')

print('\nlist length:', len(list_type),
      '\nlist content:',   list_type)


#len of a list
list_length = len(list_type)

index_of_string =list_type.index({'fruit':'apple'})
print('position of dictionary:',index_of_string)


