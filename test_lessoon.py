# Наш перший коментар
int_value = 1 # Ціле число, integer or int
negative_int_value = -1 # Ціле відємне число, integer or int
print(int_value)
print(negative_int_value)

float_value = 1.234 # Float, дробове число або чисо з плаваючою точкою
print(float_value)

print()

string_value = 'Text' # String or str стрічка with quotes
print(string_value)

string_second = "Text 2" # String or str стрічка with double quotes 
print(string_second)

print()

meaningful_sentence = "Once upon a time .... don't"
print(meaningful_sentence)

meaningful_sentence_two = 'Once upon a time .... don\'t  \\m/'
print(meaningful_sentence_two)

print()

meaningful_sentence_three = 'The First line \n\tThe Second one'
print(meaningful_sentence_three)

print()

very_long_string = 'Very long long long sentence without any sence or context' +\
'but stil this one is very long and hardly readable'
print(very_long_string)

print()

paragraph_text = """First line
second line
third line
...
last line"""
print(paragraph_text)

print()

paragraph_text_single_quotes = '''First line
second line
third line
...
last line'''
print(paragraph_text_single_quotes)

print()

negative_statement = False # False actually is 0
positive_statement = True # True actually 1

print(negative_statement)
print(positive_statement)

print()

#Calculations
x = 1
y = 2
print(x + y)
print(x - y)
print(x / y)
print(x * y)

print(x % y)

print(x // y)

print(f'Sum: {x} + {y} = {x + y}')

print(f'Ext: {x} - {y} = {x - y}')

print(f'Div: {x} / {y} = {x / y}')

print(f'Mult: {x} * {y} = {x * y}')

print(f'Modulo: {x} mod {y} = {x % y}')

print(f'Integer division: {x} // {y} = {x // y}')

print(f'Text: {paragraph_text_single_quotes}')

x = 3
y = 3
comparison_result = x == y

print(f'Comparing {x} and {y}: {comparison_result}')

print(f'Is {x} more than {y}: {x > y}')

print(f'Is {x} less than {y}: {x < y}')

print(f'Is {x} more or equal than {y}: {x >= y}')

print(f'Is {x} less or equal than {y}: {x <= y}')
