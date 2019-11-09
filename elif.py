country = input('What country are you from? ')

if country.lower() == 'canada':
    province = input("What province do you live in? ")

    if province.lower() in('alberta' ,\
        'nunavut' , 'yukon'):
        tax = 0.05
    elif province.lower() == 'ontario':
        tax = 0.13
    else:
        tax = 0.14
else: 
        tax = 0.00

print('Your tax is ' + str(tax))
