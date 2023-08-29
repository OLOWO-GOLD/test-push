#complex
#simple problems
#boolean statement input==constant (true or false)
#wrap it in if statement (if true) => (if input==constant) do...
#wrap in a for loop (for items in list{if input==constant).....})
input_variable = input("")

#save as uppercase using (string.upper())
saved_uppercase_version = input_variable.upper()
#save as lowercase
saved_lowercase_version = input_variable.lower()
#save as capitalized
saved_capitalize_version = input_variable.capitalize()

#print(input_variable) == (constant)
if input_variable == saved_uppercase_version:
    print('%s is in Uppercase' %(input_variable))
elif input_variable == saved_lowercase_version:
    print('%s is in lowercase' %(input_variable))
elif input_variable == saved_capitalize_version:
    print('{} is in capitalized case'.format(input_variable))
else:
    print('No case detected in {}'.format(input_variable))
  




#pos = int(input('Enter a number: '))
#while pos > 0: 
  #print('Positive')
 
     
          
