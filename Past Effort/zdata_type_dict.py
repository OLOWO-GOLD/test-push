#dictionary
dict_example = {'key', 'value', 'new key', 'new value'}

dict_type = {'pep id': ['name', 'address', 'phone number',
                       'last visit', 'age', 'gender'],
            'pep id new':[]} 
print('dict keys:',dict_type.keys())

#debugging
print(dict_type)

for all_keys in dict_type.values():
  print('\nall keys ',all_keys)


#create empty list
print('empty string',list())
print('empty dict', dict())

x = []
di = {}

#add new items to dict
dict_type['new key'] = 'new value'
print('updated dict',dict_type)

#length of dict
length_of_dict = len(dict_type)
print('length of dict', length_of_dict)


#Task
#create an empty dictionary and print it
#add new items to your empty details below
#{‘Electronics’:‘fan’,’clippers’:’tv’,’ups’:'radio'}
#print your new dictionary
#add anot#dictionary
dict_example = {'key', 'value', 'new key', 'new value'}

dict_type = {'pep id': ['name', 'address', 'phone number',
                       'last visit', 'age', 'gender'],
            'pep id new':[]} 
print('dict keys:',dict_type.keys())

#debugging
print(dict_type)

for all_keys in dict_type.values():
  print('\nall keys ',all_keys)


#create empty list
print('empty string',list())
print('empty dict', dict())

x = []
di = {}

#add new items to dict
dict_type['new key'] = 'new value'
print('updated dict',dict_type)

#length of dict
length_of_dict = len(dict_type)
print('length of dict', length_of_dict)



#Task
#create an empty dictionary and print it
#add new items to your empty details below
#{‘Electronics’:‘fan’,’clippers’:’tv’,’ups’:'radio'}
#print your new dictionary
#add another new item to your empty details below
#{‘Electronics’:[‘fan’,’clippers’,’tv’,’ups’]}
#print your new dictionary
#remove the value 'tv' from the dictionary
#remove the list  [‘fan’,’clippers’,’tv’,’ups’] from the dictionary here new item to your empty details below
#{'Electronics':['fan','clippers','tv',ups’]}
#print your new dictionary
#remove the value 'tv' from the dictionary
#remove the list  [‘fan’,’clippers’,’tv’,’ups’] from the dictionary

#Created an empty dict & added items to it
new_dict = {}
print('This is an empty dict', new_dict)
new_dict['Electronics'] = 'fan'
new_dict['clippers'] = 'tv'
new_dict['ups'] = 'radio'
print('Items added to the empty dict are:',new_dict)

#add another list item to your empty dictionary details below
new_dict['Electronics'] = ['fan', 'clippers','tv','ups']
print('Added list item to empty dictionary',new_dict)

#remove the value 'tv' from the dictionary
new_dict['Electronics'] = ['fan', 'clippers', 'ups']
print('Remove the value tv from the list', new_dict)

#remove the list
del new_dict['Electronics']
print('Results after removing the list',new_dict)
