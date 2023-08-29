



def length_of_string(my_data):
  counter = 0
  for item in my_data:
    if len(item) >= counter:
      counter = len(item)

  return counter

store_data = ['adewalesibitikode', 'adeyeyemi', 'adewolemitan', 'adeola']
print("The highest amount is: %i" % length_of_string(store_data))

