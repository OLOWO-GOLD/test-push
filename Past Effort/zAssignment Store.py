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
ext1 = '.py'
ext2 = '.txt'
ext3 = '.exe'
ext4 = '.pyc\n'

files = [file_name1, file_name2, file_name3, file_name4]
ext = [ext1, ext2, ext3, ext4]
for file_with_ext in files:
  for ext_items in ext:
    print(file_with_ext + ext_items)

#task 2
#add check if the following  letters exist in the file names
#check for letter "e"
#check  for letter "a"
#check  for letter "s"
#check for substring "mode"
#check for  substring  "ie"
item1 = 'e'
item2 = 'a'
item3 = 's'
item4 = 'mode'
item5 = 'ie\n'

files = [file_name1, file_name2, file_name3, file_name4]
letters_and_substring = [item1,item2,item3,item4,item5]
for itemz in files:
  for letters in letters_and_substring:
    if letters in itemz:
      print("The file: %s contains: %s" % (itemz, letters))
    else:
      print("The file: %s doesn't contain: %s" %(itemz,letters))
      

#List
cutlery  =['knives', 'spoon', 'fork']

others = ['cup', 'jug', 'pots']

#Task 1
#add new culteries  of your choice to the list
addition = ['nut_cracker', 'tin_cutter','paring_knife', 'soup_spoon']

for added in addition:
  cutlery.append(added)


#Task 2
#remove the  item  "knives"  from the list
cutlery.remove('knives') #using value  index
#find a way to  delete value using the value name
print(cutlery)

#Task 3
#add a "pan" to the second position of the  list so it would look like this  ['cup','pan', 'jug', 'pots']
others = ['cup', 'jug', 'pots']
others[1:1] = ['pan']
others.insert(1,'pan') #another  approach
print(others)

#Task 4
#combine the cultery and others list together in a new list 
 #and call the new list kitchen  items
kitchen_items = cutlery + others
print(kitchen_items)



#Dictionary
#below is a dictionary  contact with the following format
#contacts={number1:name1, number2:name2}
contacts = {803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 348934:'Error',485923:"N/A",893843:"No Name"}

#Task1
#print  out all the  keys of the dictionary
contacts_keys = contacts.keys()
print("The list of the keys in the dictionary", contacts_keys)
print('\n')
#print  out all the  values of the dictionary
contact_values = contacts.values()
print("The list of values in the dictionary", contact_values)
print('\n')

#Task 2
#if contact name has errors eg 'Anonymous', 'Uknown', 'Error', 'N/A', 'No Name'  in it remove it
error_items = ['Anonymous', 'Unknown', 'Error', 'N/A', 'No Name']
for key ,value in list(contacts.items()):
  if value in error_items:
    del contacts[key]
print("All the errors have been filtered out and remains", contacts)
print('\n')

#Task 3
#if  length of  contact number is greater than 6 remove it
#create a list of all removed  items in this format
#removed_items =['number1 name1',   'number2 name2']
#eg removed_items =['894545 John Doe', '344934 Unknown']
removed_items = []
for key, value in list(contacts.items()):
  if len(str(key)) > 6:
    removed_items.append(f"{key} {value}")
    del contacts[key]
print("Removed_items", removed_items)
  

#Dictionary
#below is a dictionary  contact with the following format
#contacts={number1:name1, number2:name2}
contacts = {803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 348934:'Error',485923:"N/A",893843:"No Name"}

#Task1
#print  out all the  keys of the dictionary
contacts_keys = contacts.keys()
print("The list of the keys in the dictionary", contacts_keys)
print('\n')
#print  out all the  values of the dictionary
contact_values = contacts.values()
print("The list of values in the dictionary", contact_values)
print('\n')

#Task 2
#if contact name has errors eg 'Anonymous', 'Uknown', 'Error', 'N/A', 'No Name'  in it remove it
error_items = ['Anonymous', 'Unknown', 'Error', 'N/A', 'No Name']
for key ,value in  list(contacts.items()):
  if value in error_items:
    del contacts[key]
print("Keys with errors filtered out & remains non error:", contacts)
print('\n')

#Task 3
#if  length of  contact number is greater than 6 remove it
#create a list of all removed  items in this format
#removed_items =['number1 name1',   'number2 name2']
#eg removed_items =['894545 John Doe', '344934 Unknown']
removed_items = []
for key, value in list(contacts.items()):
  if len(str(key)) > 6:
    removed_items.append(f"{key} {value}")
    del contacts[key]
print("Removed_items", removed_items)


#arithmetic progress
#common difference
#arithmetic_progression = [1,2,3,4,5,6,7,8]
#2-1 =1
#3-2 = 1
#4-3= 1
#5-4 = 1
#6-5 = 1
#common_difference_AP=([2,3,4,5])
#common_difference = 1
#even numbers
#arithmetic_progression = [2,4,6,8,10]
#odd numners
#arithmetic_progression = [1,3,5,7,9]

def common_difference_AP(Arithmetic_Progression):
  ...
  
  
#common_difference =  5
#give me first 10 numbers of this progression starting  #from 1
#1, 6, 11, 16, 19, 24, 29, 34
#def common_difference_AP(Arithmetic_Progression):
#data = 
  
#1 ,1 , 2,3,5,8,13
#50th count

#Task 7
#write a function to  evaluate common difference of any arithmentic  progression. your function will take list of arithmetic progression. for example 
#Arithmetic_Progression = [1, 2, 3, 4]
#def common_difference(Arithmetic_Progression):
#use the arithmetic progression below  to test your code.   
#1,2,3,4,5
#2,4,6,8,10
#1,3,5,7,9

arithmetic_progression1 = [1, 2, 3, 4, 5]
arithmetic_progression2 = [2, 4, 6, 8, 10]
arithmetic_progression3 = [1, 3, 5, 7, 9]

def common_difference(Arithmetic_Progression): #place holder, it could be called (olowogold)
  '''Applying Recursion method'''  
  difference = Arithmetic_Progression[1] - Arithmetic_Progression[0]
  return difference
  
difference1 = common_difference(arithmetic_progression1)
difference2 = common_difference(arithmetic_progression2)
difference3 = common_difference(arithmetic_progression3)

print("The common difference is:", difference1)
print("The common difference is:", difference2)
print("The common difference is:", difference3)   

#Task 8
#write a function to evaluate common ratio in a  geometric progression
#According to standard maths, a geometric progression or a geometric sequence
#is the sequence, in which each term is varied by another by a common ratio.
#Examples:[2,4,8,16,32,64]
#common ratio is:
#4/2 = 2
#8/4 = 2
#16/8 = 2
#32/16 = 2
#64/32 = 2
#write the code

geometric_progression1 = [2,4,8,16,32,64]
geometric_progression2 = [3,9,27,81,243]
geometric_progression3 = [4,16,64,256,1024]

def common_ratio(geometric_progression):
  '''Applying Recursion method''' 
  ratio = geometric_progression[1] / geometric_progression[0]
  return ratio

ratio1 = common_ratio(geometric_progression1)
ratio2 = common_ratio(geometric_progression2)
ratio3 = common_ratio(geometric_progression3)

print("The common ratio is:",int(ratio1))
print("The common ratio is:",int(ratio2))
print("The common ratio is:",int(ratio3))  


#Task 9
#write function to  evaluate conditional statement in excel. 
#for example: if(logical_statement, result_if_true, result_if_false)

#Logical_statements
Toyota_corrola_price = 1000
Toyota_lexus_price = 2000

def vehicle_price(Toyota_cars):
#if(logical_statement, result_if_true, result_if_false) 
  if Toyota_corrola_price != Toyota_lexus_price:
    return True
  else:
       return False
Cars = vehicle_price("Toyota_cars")
print(Cars)




#functions
#wrap code in a group and isolate from others
print(5+5)
print('main script')


def sum(a,b):
  
  """This function adds two numbers together"""
  
  print('------------------\nadd function')
  output =a + b
  return output
  
#add = sum()
#print(add)


def sum(input1, input2):
  output=input1+input2
  print(output)

#sum(4,5)


#Task 1
#write a function to sum  two values and print the result
#for example: sum(a,b) print (a+b)

#Task 2
#write a function  to subtract two values and print the result

#Task 3
#write a function to multiply two value and print  the result

#task 4 
#write a function to divide two values and  print  the result
#write a function to calculate the area of a triangle and return the result

#Task 5
#write a function to evaluate fibonacci  sequence

#Task 6
#write a function to  evaluate common difference   in an arithmentic progression

#Task 7
#write a function to evaluate common ratio  in a  geometric progration


#Task 8
#write function to  evaluate conditional statement in excel. 
#for example: if(logical_statemen, result_if_true, result_if_false)






