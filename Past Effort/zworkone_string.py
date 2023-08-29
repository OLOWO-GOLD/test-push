#Task
#write a script to check the case of the strings below
#your answer will be in the form of: capital case, lower case, upper case
#hint   
#name = 'Gold'
#answer: capital case

#Questions:
variable_name = 'Sum'
operator_name = 'PLUS'
result_returnd = 'five'
edge_cases = 'Minus Five'
unknown = 'undefined'

case = "OLOWOGOLD"

#to compare, we need two values
#we compare with boolean expressions that give boolean result (True or False)
#we need a point of reference to compare

#Algorithm 1
#step 1: get an NLP (natural language processing) API (Application Programming Interface) to convert my spoken commands to text data
#step 2: chat GPT will accept text data and process then return text result (GPT API)
#step 3: NLP API convert text result back to spoken words

#Algorithm 2
input_variable ='olowogold'
converted_to_upper = input_variable.upper()
input_variable == converted_to_upper

if variable_name == case:
 print("capital case")
elif operator_name == case:
  print("upper case")
elif result_returnd == case:
  print("lower case")
elif edge_cases == case:
  print("capital case")
elif unknown == case:
  print("lower case")
else:
  print("No case")


print('----------------------------')

#Task
#split the strings into lists
# Question:
with_new_lines = 'new\nlines\n' #remove the new lines
with_tabs = 'with\ttabs'  # the tables
with_html = '<strong>New string</strong>' #remove the html code <strong> and </strong>
extra_html_code = '<p>Print out the paragraphs</p>' #REMOVE THE <>

if '' in with_new_lines:
  lin = with_new_lines.translate({ord('\n'): None})
  lis = lin.split(' ')
  print(lis)


with_tabs = 'with\ttabs' 
rem = ['\t']
for tab in rem:
  with_tabs = with_tabs.replace(tab,'')
  space = with_tabs.split(' ')
print(space)


with_html = '<strong>New string</strong>'
remove = ['<strong>','</strong>']
for val in remove:
  with_html = with_html.replace(val,'')
  web = with_html.split(' ')
print(web)


extra_html_code = '<p>Print out the paragraphs</p>'
remov = ['<p>','</p>']
for data in remov:
  extra_html_code = extra_html_code.replace(data, '')
  gprs = extra_html_code.split(' ')
print(gprs)


#write a script to check if a number is positive, negative or none

(-5, -4, -3, -2 , -1,) < 0 > (1, 2, 3)
#algorithm
#step 1: Use if statement
#step 2: if positive return / print +ve
#step 3: if negative return / print -ve
#step 4 : if none return / print None
#explanation
#booleans with if statement to check / test
#boolean expressions- a== b, a > y , t>= y, e!= u give True / false
#combine boolean with if statement
#if True: do something, if False: do something

pos = input(int())
if pos > 0:
  print(True)
elif pos < 0:
  print(False)
else:
  print(None)
  


"https://www.youtube.com/watch?v=MS0U3JIb234"
  


#argument, 
'''
for val in remove:
  with_html = with_html.replace(val,'')
  web = with_html.split(' ')
print(web)
'''

"""
rem = ["\n"]
for lin in rem:
    with_new_lines = with_new_lines.replace(lin,'')
    new_ = with_new_lines.split(' ')
print(new_)
"""

'''
rem = ['\t']
for tab in rem:
  with_tabs = with_tabs.replace(tab,'')
  space = with_tabs.split(' ')
print(space)
'''

'''
remov = ['<p>','</p>']
for data in remov:
  extra_html_code = extra_html_code.replace(data, '')
  gprs = extra_html_code.split(' ')
print(gprs)
'''

compound = [1, 43, 4590, 'key', 'value', 'pair'] 

#tuple

for content in enumerate(compound):
  position,  value = content 
  #print(position, value)
  #print("Position_of_compound_values:",content)

compound = [1, 43, 4590, 'key', 'value', 'pair'] 
for position, value in enumerate(compound):
  print("Position of %s in the list - compound:" %value ,'is', position)
  
"""for val in enumerate(complex):
     print("Position_of_complex_values",val)

for things in enumerate(common_):
  print("Position_of_common_value", things)
"""
