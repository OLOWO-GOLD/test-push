#String
#split
new_string = 'un defined'
print('string',  new_string)
print('list',  new_string.split(' '))

#Task
#split the strings into lists
# Question:
with_new_lines = 'new\nlines\n' #remove the new lines
with_tabs = 'with\ttabs'  # the tables
with_html = '<strong>New string</strong>' #remove the html code <strong> and </strong>
extra_html_code = '<p>Print out the paragraphs</p>' #REMOVE THE <>

lines = r"""OlowoGold
Oluwatosin
Idris
"""

'''
new_lines_split = lines.split("\n")
print("new lines", lines)
'''

with_new_lines = 'new\nlines\n'
splitted_with_new_lines = with_new_lines.split('\n')
print("splitted_with_new_lines:",splitted_with_new_lines)



with_tabs = 'with\ttabs' 
tabs = with_tabs.split('\t')
print("without_tabs:", tabs)



#splitted_in_list = with_html.split(' ')
#joined_list = '_'.join(splitted_in_list)
"""
strin = '''Dear_Olowogold_Oluwatosin,
I_write_inform_you_of_our.....
'''
splitted_into_list = strin.split('_')
print('splitted_in_list:',splitted_into_list)
list_2_strin = ' '.join(splitted_into_list)
print('list to strin:', list_2_strin)
cleaned_list = list_2_strin.split('.')
print('cleaned list:', cleaned_list)
convert_to_string_data_type = ' '.join(cleaned_list)
print('convert_to_string_data_type:',convert_to_string_data_type)
"""



"""
<html>

  <head>
    <Title>
      Olowogold's Website
    </Title>
  </head>
  
  
  <body>
    <div>
      <h1>
      Olowogold's Website
      </h1>
    </div>
    <div>
    
      <strong>
      I am Olowogold
      </strong>
    </div>
  </body>
  </html>
"""

with_html = '<strong>New string</strong>'
with_html = with_html.split('<strong>')
joined_html = ' '.join(with_html)
without_strong = joined_html.split('</strong>')
print('without_html', without_strong)


#p tag is paragraph tag
extra_html_code = '<p>Print out the paragraphs</p>'
extra_html_code = extra_html_code.split('<p>')
joined = ''.join(extra_html_code)
new_paragraph = joined.split('</p>')
print("printing_out:", new_paragraph)
