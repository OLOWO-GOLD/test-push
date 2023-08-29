Category = ['fruit', 'sales', 'food', 'gadgets']

Miscelleneous = [
  'fruit orange', 'food Fried_rice', 'sales 34400', 'sales 56834',
  'gadgets PDA', 'fruit apple', 'fruit pear', 'food yam'
]
'''
Problem:
Use the Category and Miscelleneous list to categorise the items.
Hint:
Dictionary = {key:value}
Dict = {Category:[items]}
Categorised = {‘Electronics’:[‘fan’,’clippers’,’tv’,’ups’]}
'''

categorised_items = {}

# Add categories to dictionary
for category in Category:
  categorised_items[category] = []

# Categorize items
for item in Miscelleneous:
  category, content = item.split(' ')
  categorised_items[category].append(content)

print(categorised_items)
