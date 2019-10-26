province = input("what province do yo ulive in ")
tax = 0

if province == 'Alberta':
    tax = 0.05
elif province == 'Nanavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else: 
    tax = .15
print(tax)

