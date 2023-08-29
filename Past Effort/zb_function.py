#Task 1
#write a function to estimate simple interest
def simple_interest(principal, rate, time):
  simple_interest_ = (principal*rate/100 * time)
  return simple_interest_

#principal = int(input("Principal Amount:"))
#rate = int(input("Percentage:"))
#time = int(input("Years:"))

#amount = simple_interest(principal, rate, time)
#print("The total simple_interest value is:",float(amount))


#Task 2
#write a function to estimate compound interest

def compound_interest(principal, rate, time):
  CI = principal*(pow((1+rate/100), time))
  return CI
  
#principal = int(input("Compound_Principal Amount:"))
#rate = int(input("Percentage:"))
#time = int(input("Years:"))

#total_amount = compound_interest(principal, rate, time)
#print("The compound_interest value is:",round(total_amount-principal, 2))

#Task 3
#write a function to all extract emails from a string, count and list them out

strin_ = """In todays digital age, technology has transformed various aspects of our lives. From communication to transportation, education to healthcare, technology has become an integral part of our society. This essay aims to explore the impact of technology on society, highlighting both its positive and negative effects. Email: (sarah_brown@example.com., alexmartinez@example.com, jenniferadams@example.com, lisa_walker@example.com, davidthompson@example.com  s made a positive impact is communication. Email, for instance, has revolutionized the way we connect with others. The speed and convenience of sending emails (johnsmith@example.com, sarahbrown@example.com, alexmartinez@example.com, jenniferadams@example.com, lisawalker@example.com) have made it a popular choice for both personal and professional communication. People from different corners of the world can now exchange messages instantly, fostering global connections and breaking down barriers and quality of education. Online learning platforms have made education more accessible to people of all ages and backgrounds. Students can now access educational resources, participate in virtual classrooms, and collaborate with peers from anywhere in the world. This democratization of education has the potential to empower individuals and bridge educational gaps. davidthompson@example.com, jenniferadams@example.com, lisawalker@example.com, sarahbrown@example.com, alexmartinez@example.com 
 On the other hand, technology has also brought about certain challenges. One of these challenges is the potential for privacy breaches and cyber threats. As we rely more on technology for communication and storage of sensitive information, the risk of unauthorized access and data breaches (davidthompson@example.com, jenniferadams@example.com, lisa_walker@example.com, sarahbrown@example.com, alexmartinez@example.com) becomes a significant concern. Protecting personal and confidential information has become crucial in the digital era. Email: jenniferadams@example.com, sarahbrown@example.com, alexmartinez@example.com, lisawalker@example.com, davidthompson@example.com  Furthermore, technology has greatly impacted the job market. Automation and artificial intelligence have led to the displacement of certain job roles, while creating new opportunities in emerging industries. The rapid pace of technological advancements (jenniferadams@example.com, sarahbrown@example.com, alexmartinez@example.com, lisawalker@example.com, davidthompson@example.com) requires individuals to adapt and acquire new skills to remain competitive in the workforce.  In conclusion, technology has had a profound impact on society, revolutionizing various aspects of our lives. While it has brought about numerous benefits in terms of communication, education, and job opportunities, we must also address the challenges that come with it, such as privacy concerns and job displacement. It is essential to strike a balance between embracing technological advancements and ensuring that they are used ethically and responsibly. Email: sarahbrown@example.com, alexmartinez@example.com, lisawalker@example.com, davidthompson@example.com, jenniferadams@example.com"""

count = 0
fruits  =['apples','ornages','mangoes']
for fruit in fruits:
  count += 1
  #print(count)


def extract_mail(strin_):
  result = " "
  count = 0
  time = 12399
  year = 2023
  quality= 10
  date= 238490
  for  string in strin_.split(" "):
    #print(string)
    if '@' in string:
      count +=1
      time += 1
      date += 1
      year += 1
      quality +=  1
      result += f"\n {time} {date} {year} {quality} {string}" 
      #print(count , string)
    
  return result
check = extract_mail(strin_)
#print(check)



import re

def regex_extract(strin_):
  pattern = r'\b[A-Za-z0-9_.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z.]{2,}\b'
  search_parameter = strin_
  result = re.findall(pattern,search_parameter)
  for olowogold, email in enumerate(result):
    print(olowogold+1, '. ', email)
  return result
#reg = regex_extract(strin_)

#print(len(reg)) 
  


#Task 4 
#write a function to check  if  a string is capitalize, lowercase or uppercase


def check_word_case(input_variable):
  
  input_variable = input("Type in string: ")
  saved_uppercase_version = input_variable.upper()
  saved_lowercase_version = input_variable.lower()
  saved_capitalize_version = input_variable.capitalize()
  

  if input_variable == saved_uppercase_version:
    result = '%s is in Uppercase' %(input_variable)
  elif input_variable == saved_lowercase_version:
    result = '%s is in lowercase' %(input_variable)
  elif input_variable == saved_capitalize_version:
    result = '{} is in capitalized case'.format(input_variable)
  else:
    result = 'No case detected in {}'.format(input_variable)
    
  return result
#cases = check_word_case('input_variable')
#print(cases)


#Task  5
#write a function to remove only the alphabetic words from  a string.
#for example:
#string:  Olowogold Oluwatosin idgold07@gmail.com  08033772678
#alphabet:  Olowogold Oluwatosin



def remove_alphabetic_words(string):
  removed_alphabets = []
  string = """*11.00am prompt.**Silk Road Restaurant, Sinoki House,* ,5th Floor, Plot 770, Off Samuel Ademulegun Avenue, Opp. Federal Ministry of Transport, CBD"""
  words = string.split(" ")
  for letter in  words:
    if letter.isalpha():
      alpha = letter
      removed_alphabets.append(alpha)
      result = " ".join(removed_alphabets)  
    
  return result
  
final_result = remove_alphabetic_words('string')
print(f"The extracted alphabets are: {final_result}" .format())


#Task  6
#write a function to remove only the numbers from  a string.
#make use placeholders  in your function
#for example:
#string:  Olowogold Oluwatosin idgold07@gmail.com  08033772678
#numbers:  08033772678
#remember, the examples are meant to test your code  after you've writen it. not to write your code


def remove_numbers(strin):
  removed_digit = []
  strin = """*11.00am prompt.**Silk Road Restaurant, Sinoki House,* ,5th Floor, Plot 770 , Off Samuel Ademulegun Avenue, Opp. Federal Ministry of Transport, CBD"""
  digit = strin.split(" ")
  for num in digit:
    if num.isnumeric():
     numbers = str(num)
     removed_digit.append(numbers)
     results = " ".join(removed_digit)
         
  return results

end_result = remove_numbers('strin')
print(f"The extracted numbers are: {end_result}".format())


  
  
  