country = input("What country do you live in? ")

if country.lower() == 'Canada':
    province = input("What province/state do you live in? ")
    if province.lower() in('Alberta','Nunavut','Yukon'):
        tax = 0.05
    elif province.lower() == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)