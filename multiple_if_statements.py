province = input("what province do you live in ")
tax = 0

if province in('Alberta','Nanavut','Yukon'):
    tax = 0.05 
elif province == 'Ontario':
    tax = 0.13
else: 
    tax = .15
print(tax)