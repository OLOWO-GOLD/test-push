#write a simple script to check if a string is capitalized, in lowercase or uppercase


#Algorithm is a set of steps you follow to approach a problem
#step 1: write a boolean expression
#step 2: wrap in a condition
#step 3: include a counter

#Talk back virtual assistant
#step 1: use nlp api to create speak to text for the gpt api
#step 2: gpt api processes text instruction and returns solution
#step 3: gpt solution converted from text back to speak with nlp


print('This is a script to check text case')
case_variable = input('Enter your text here: ')

#check for uppercase
variable_upper_version = case_variable.upper()
#check for lowercase
variable_lower_version = case_variable.lower()
#check for capitalized
variable_capitalized_version = case_variable.capitalize()

if case_variable == variable_upper_version:
    print("This is an uppercase")
if case_variable == variable_lower_version:
    print("This is a lowercase")
if case_variable == variable_capitalized_version:
    print("This is capitalized case")

#boolean: 
current_amount = 20
new_credit = 5000000000000
current_amount = current_amount + new_credit
#boolean expression
boolean_result = current_amount>2000000

if current_amount>2000000:
  #evaluate
  ...
else:
  ...


  
  



if (5>3):
  #do something
  ...





