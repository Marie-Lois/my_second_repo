"""
Checks whether a customer can afford a product
at a supermarket.
"""

item = str(input("Enter Item: "))
price = float(input("Enter Price of Item: "))
momo_balance = float(input("Enter momo_balance Balance: "))
charges = round(2/100 * price, 2)


if momo_balance > 0:
    if momo_balance >= price + charges:
        print(f"Successful purchase of {item}")
    else:
        print("Insufficient balance")
else:
    print("Your momo is empty sha")




# if momo_balance < price:
#     print("Your balance is insufficient")
# elif momo_balance == price:
#     print("Insufficient Charges for withdrawal")
# elif momo_balance < momo_balance + charges:
#     print("Please refill upto 2% of price")
# elif momo_balance > 2 / 100 price:
#     print("Enter momo_balance pin to pay for item")
# else:
#     print("Item Can't be Purchased")
