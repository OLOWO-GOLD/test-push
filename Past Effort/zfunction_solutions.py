#Task 1
#write a function to sum  two values and print the result
#for example: sum(a,b) print (a+b)
def addition(k,g):
  input = k+g
  return input

add = addition(30,20)
print("The additional result is:",add)


#Task 2
#write a function  to subtract two values and print the result

def subtraction(k,g):
  input = k-g
  return(input)
  
minus = subtraction(30,20)
print("The subtraction  result is:",minus)


#Task 3
#write a function to multiply two value and print  the result
def multiply(k,g):
  input = k*g
  return input
multiply = multiply(30,20)

print("The multiplication result is:",multiply)


#task 4 
#write a function to divide two values and  print  the result


def divide(k,g):
  input = k/g
  
  return(input)
divide = divide(30,2)
print("The division result is : %.0f" % divide)


#Task 5
#write a function to calculate the area of a triangle and return the result



def area_of_triangle(base,height):
  
  "formula: half(base*height)"
  
  dividend = divide(1,2)
  dividend_6_7 = divide(6,7)
  dividend_20_25 = divide(20,25)
  area  =  1/2 * 6/7 *  20/25
  area  = divide * dividend_6_7 * dividend_20_25
  
  area = dividend * base * height
  return area


base = int(input("base: "))
height = int(input("height: "))

area = area_of_triangle(base,height)
print("area answer is: %.1f" % area) 


#Task 6
#write a function to list the first 50 numbers in fibonacci  sequence


import math

def PerfectSquare(x):
  s = int(math.sqrt(x))
  return s*s==x
  
n = int(input("enter the number: "))
result1 = 5*(n*n)+4
result2 = 5*(n*n)-4
if PerfectSquare(result1) or PerfectSquare(result2):
  print(n,"is fibonacci number")
else:
  print(n,"is not fibonacci number")


#1 ,1 , 2,3,5,8,13
#50th count



#Task 7
#write a function to  evaluate common difference of any arithmentic progression e.g 
#1,2,3,4,5
#2,4,6,8,10
#1,3,5,7,9











#Task 8
#write a function to evaluate common ratio  in a  geometric progration

#Task 9
#write function to  evaluate conditional statement in excel. 
#for example: if(logical_statement, result_if_true, result_if_false)


















