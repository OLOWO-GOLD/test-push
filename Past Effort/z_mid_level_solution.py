def sum(a,b):
  #logic
  result = a+b
  return result

def subtract(a,b):
  result = a-b
  return result

total = subtract(15,5)
#print(total)

def multiply(a,b):
  result = a*b
  return result

total = multiply(5,8)
#print(total)

def divide(a,b):
  result = a/b
  return result

total = divide(8,2)
#print(total)

def raise_to_power_of(a,b):
  result = a**b
  return result

total = raise_to_power_of(5,4)


#print(4+5*0.25+7/20**2)

def calculate(arguments):   #Area of Concentration
  arguments_list = []
  for num, var in enumerate(arguments.split(',')):
    if var:
      arguments_list.append(float(var.strip()))
      #print(float(var.strip()))
      
  a = arguments_list[0]
  b = arguments_list[1]
  c = arguments_list[2]
  d = arguments_list[3]
  e = arguments_list[4]
  f = arguments_list[5]
  g = arguments_list[6]
    
  
  add = sum(a,b)
  times = multiply(add,c)
  minus = subtract(times,d)
  quotient = divide(minus,e)
  total = raise_to_power_of(quotient,sum(f,g))
  #total = sum(2,3) + 20
  return total          #Area of Concentration


def create_arguments(question):
  special_operator = "**"
  operators = ['+','*','-','/','(','+',')']
  
  special_splitted = question.split(special_operator)
  special_join = ''.join(special_splitted)
  #print(special_join)
  
  
  for  operator in operators:
    list_split =  special_join.split(operator)
    special_join  = ','.join(list_split)
    
  return  special_join

bulk_string="""3.2 + 4.6 * 0.7 - 9 / 2.1 ** (5 + 3)
6 + 8 * 0.9 - 12 / 3.5 ** (2 + 4)
1.7 + 2.3 * 0.6 - 4 / 1.8 ** (3 + 5)
9 + 11 * 0.8 - 15 / 2.6 ** (4 + 2)
2.5 + 3.8 * 0.5 - 7 / 1.9 ** (1 + 6)
4 + 6 * 0.7 - 8 / 2.2 ** (2 + 4)
5.1 + 7.9 * 0.4 - 10 / 2.5 ** (3 + 3)
7 + 9 * 0.9 - 13 / 3.8 ** (4 + 2)
0.8 + 1.2 * 0.6 - 3 / 1.4 ** (5 + 1)
8 + 10 * 0.8 - 14 / 2.7 ** (2 + 5)
3.4 + 5.6 * 0.5 - 9 / 2.3 ** (4 + 3)
5 + 7 * 0.7 - 11 / 2.9 ** (1 + 6)
2.1 + 3.9 * 0.4 - 6 / 2.2 ** (3 + 4)
7 + 9 * 0.9 - 13 / 3.5 ** (2 + 5)
1.5 + 2.7 * 0.6 - 5 / 1.9 ** (4 + 3)
9 + 10 * 0.8 - 14 / 2.4 ** (3 + 4)
3.8 + 5.2 * 0.5 - 8 / 2.1 ** (2 + 6)
6 + 8 * 0.7 - 11 / 2.8 ** (4 + 3)
2.3 + 4.7 * 0.4 - 7 / 2.3 ** (1 + 5)
7 + 9 * 0.9 - 13 / 3.2 ** (3 + 4)
1.7 + 3.3 * 0.6 - 6 / 1.8 ** (2 + 6)
9 + 10 * 0.8 - 14 / 2.5 ** (4 + 2)
4.5 + 5.5 * 0.5 - 8 / 2.2 ** (3 + 5)
6 + 8 * 0.7 - 11 / 2.9 ** (2 + 5)
2.2 + 4.8 * 0.4 - 7 / 2.4 ** (1 + 6)
7 + 9 * 0.9 - 13 / 3.1 **(3 + 5)
1.9 + 3.1 * 0.6 - 6 / 1.7 ** (2 + 6)
9 + 10 * 0.8 - 14 / 2.6 ** (4 + 2)
5.8 + 6.2 * 0.5 - 8 / 2.3 ** (3 + 4)
6 + 8 * 0.7 - 11 / 2.8 ** (2 + 5)
2.5 + 4.5 * 0.4 - 7 / 2.5 ** (1 + 6)
7 + 9 * 0.9 - 13 / 3.3 ** (3 + 4)
2.1 + 3.9 * 0.6 - 6 / 1.9 ** (2 + 6)
9 + 10 * 0.8 - 14 / 2.4 ** (4 + 3)
5.2 + 5.8 * 0.5 - 8 / 2.2 ** (3 + 5)
6 + 8 * 0.7 - 11 / 2.9 ** (2 + 4)
2.3 + 4.7 * 0.4 - 7 / 2.1 ** (1 + 5)
7 + 9 * 0.9 - 13 / 3.2 ** (3 + 5)
1.8 + 3.2 * 0.6 - 6 / 1.6 ** (2 + 6)
9 + 10 * 0.8 - 14 / 2.5 ** (4 + 2)
4.6 + 5.4 * 0.5 - 8 / 2.3 ** (3 + 4)
6 + 8 * 0.7 - 11 / 2.8 ** (2 + 5)
2.4 + 4.6 * 0.4 - 7 / 2.4 ** (1 + 6)
7 + 9 * 0.9 - 13 / 3.1 ** (3 + 5)
1.9 + 3.1 * 0.6 - 6 / 1.7 ** (2 + 6)
9 + 10 * 0.8 - 14 / 2.6 ** (4 + 2)
5.5 + 4.5 * 0.5 - 8 / 2.1 ** (3 + 5)
6 + 8 * 0.7 - 11 / 2.9 ** (2 + 4)
2.2 + 4.8 * 0.4 - 7 / 2.5 ** (1 + 6)
7 + 9 * 0.9 - 13 / 3.3 ** (3 + 4)"""

bulk=bulk_string.split('\n')
for index,question in  enumerate(bulk):
  arguments= create_arguments(question) 
  result =calculate(arguments)
  print('question:{}. '.format(index+1),question,'\nanswer:  ',result,'\n\n')