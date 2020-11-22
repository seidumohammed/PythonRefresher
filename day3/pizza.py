print("Welcome to Halal Pizza")
order = input("Place an order: ")

if order == "S":
    bill = 5
elif order == "M":
    bill = 10
wants_peperoni = input("Wants peperoni ?: ")
if wants_peperoni == "Y":
    if order == "M":
        bill += 3
    else:
        bill += 2

wants_extra_cheese = input("Wants extra cheese ? : ")
if wants_extra_cheese == "Y":
    bill += 1

print(f"Total bill is ${bill}")
