#string task

file_name1 = 'main'
file_name2 = 'test'
file_name3 = 'view'
file_name4   = 'models'

#task 1
#add the following extension  to the filenames  
#add .py
#add .txt
#add .exe
#add .pyc

#task 2
#add check if the following  letters exist in the file names
#check for letter "e"
#check  for letter "a"
#check  for letter "s"
#check for substring "mode"
#check for  substring  "ie"


#List

cutlery  =['knives', 'spoon', 'fork']

others = ['cup', 'jug', 'pots']

#Task 1
#add new culteries  of your choice to the list
#Task 2
#remove the  item  "knives"  from the list

#Task 3
#add an "pan" to the second position of the  list so it would look like this  ['cup','pan', 'jug', 'pots']
#Task 4
#combine the cultery and others list together in a new list 
 #and call the new list kitchen  items


#Dictionary
#below is a dictionary  contact with the following format
#contacts={number1:name1, number2:name2}

contacts = {803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 348934:'Error',485923:"N/A",893843:"No Name"}

#Task1
#print  out all the  keys of the dictionary
#print  out all the  values of the dictionary

#Task 2
#if contact name has  error  in it remove it

#Task 3
#if  length of  contact number is greater than 6 remove it
#create a list of all removed  items in this format
#removed_items =['number1 name1',   'number2 name2']
#eg removed_items =['894545 John Doe', '344934 Unknown']





#Tutor's examples
first = 'first'
second = 'second'

add = 'item1'
next = 'next'

#output :
#firstitem1
#firstitem2
#seconditem1
#seconditem2

first_list = [first, second]
second_list  = [add, next, 'olowogold', 'tosin','idris','sfi','sdfio','dsfj','sfj\n']

#first approach: dynamic approach
print('first approach: dynamic approach\n')
for first_items in  first_list:
  for second_items in second_list:
    print(first_items+ '_' + second_items)


#second approach: static approach
print('second  approach: static approach\n')
for first_items in  first_list:
  print(first_items+  '_' + second_list[0])
  print(first_items+   '_' + second_list[1])
  print(first_items+  '_' + second_list[2])
  print(first_items+  '_' + second_list[3])
  print(first_items+  '_' + second_list[4])
  print(first_items+  '_' + second_list[5])
  print(first_items+  '_' + second_list[4])












































