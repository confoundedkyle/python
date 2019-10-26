first_name = input('Please Enter Your First Name: ')
last_name = input('Please Enter Your Last Name: ')

output = 'Hello, ' + first_name + ' ' + last_name
output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {0} {1}'.format(first_name, last_name)
# Only available in Python 3
output = f'Hello, {first_name} {last_name}'

print(output) 