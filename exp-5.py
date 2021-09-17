price = int(input("Enter the price: "))
has_good_credit = bool(input("Does have a good credit or not: "))
if has_good_credit == "True":
    down_payment = 0.1 * price
if has_good_credit == "False":
    down_payment = 0.2 * price
print(f"{down_payment} ")
