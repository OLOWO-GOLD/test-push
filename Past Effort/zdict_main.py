#Dictionary
#below is a dictionary  contact with the following format
#contacts={number1:name1, number2:name2}
contacts = {803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 348934:'Error',485923:"N/A",893843:"No Name"}

#Task1
#print  out all the  keys of the dictionary
print("The entire keys in the contacts are:",contacts.keys())

#print  out all the  values of the dictionary
print("The entire values in the contacts are:",contacts.values())

#Task 2
#if contact name has  error  in it remove it
del contacts[348934]
print("Removing the key with error and printing out the remains", contacts)


#Task 3
#if  length of  contact number is greater than 6 remove it

#create a list of all removed  items in this format

#removed_items =['number1 name1',   'number2 name2']
#eg removed_items =['894545 John Doe', '344934 Unknown']