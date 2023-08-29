#Dictionary
#below is a dictionary  contact with the following format
#contacts={number1:name1, number2:name2}
contacts = {803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 348934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 348934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 3438934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 3468934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 3482934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34893234:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34834934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34845934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34823934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34893124:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34845934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 346568934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34678934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34678934:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34891334:'Error' ,485923: "N/A", 893843 :"No Name",803366472 :'John Doe', 703432302:'Jane Doe', 378232:'Anonymous',  7382032:'Unknown', 34889934:'Error' ,485923: "N/A", 893843 :"No Name",}

#Task1
#print  out all the  keys of the dictionary
print('The contact keys only', contacts.keys())
print('\n')

#print  out all the  values of the dictionary
print('The contact values only', contacts.values())
print('\n')

#Task 2
#if contact name has  error in it remove it
removed_error = 'Error'
contact_keys = contacts.keys()

errors = []
for key in contact_keys:
  value = contacts[key]
  if removed_error in value:
    errors.append(key)
    
for keys in errors:
  contacts.pop(keys)

print(contacts)
  
print('\n')

#alternative approach

list_of_errors = []

for key, value in contacts.items():
  if 'Error' in value:
    list_of_errors.append(key)

for key_errors in list_of_errors:
  contacts.pop(key_errors)


#simplers approach

cleaned_contacts = {}
for key, value in contacts.items():
  if 'Error' not in value:
    cleaned_contacts[key] = value


contact_dict =  {'idrisgold07@gmail.com':'Olowogold OluwaTosin', 'brightoadewole@gmail.com':'Bright Adewole','johndoe@unknown.com':'John Doe', 'anonymous@yahoo.com':'Anonymous','unknown@ymail.com':'Uknown Mail'}

for email, name  in contact_dict.items():
  print(email, name)
  if 'error' in name:
    print(email)







  



#Task 3 
#if  length of contact number is greater than 6 remove it


#create a list of all removed  items in this format
#removed_items =['number1 name1',   'number2 name2']
#eg removed_items =['894545 John Doe', '344934 Unknown']









