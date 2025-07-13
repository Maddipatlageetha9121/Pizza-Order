size=input("size of your pizza (S/M/L)?\nsize=")
bill=0
if size == 's' or size =='S':
    price=100
    bill +=price
    print(f"small size pizza price is {price} RS.")
elif size == 'M' or size == 'm':
    price=200
    bill +=price
    print(f"medium size pizza price is {price} RS.")
else:
    price=300
    bill +=price
    print(f"large size pizza price is {price} Rs.")
add_pepperoni=input("Do you want pepperoni(Y/N)?\npepperoni=")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        price =30
        bill+=price
        print(f"pepperoni price for small size pizza is {price} Rs.")
    elif size =='m' or size =='M':
        price=45
        bill +=price
        print(f"pepperoni price for medium size pizza is {price} Rs.")
    else:
        price=60
        bill +=price
        print(f"pepperoni price for large size pizza is {price} Rs.")
extra_cheese=input("Do you want extra cheese(Y/N)\nextra cheese=")
if extra_cheese == 'Y' or extra_cheese == 'y':
    if size =='s' or size =='S':
        price=30
        bill +=price
        print(f"cheese price for small size pizza is {price} Rs.")
    elif size =='m' or size =='M':
        price=45
        bill +=price
        print(f"cheese price for medium size pizza is {price} Rs.")
    else:
        price=60
        bill +=price
        print(f"cheese price for large size pizza is {price} Rs.")
print(f"your final bill is {bill} RS.")