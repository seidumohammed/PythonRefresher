print("Welcome to the tip calculator !")
bill = float(input("What is the total bill: $"))
tip = int(
    input("What % tip would you like to give:10, 12 or 15: "))
people = int(input("How many people to split the bill ?"))

bill_with_tip = round((bill*(1 + tip/100)), 2)
tip_percent = bill * (tip/100)
total_tip = round((tip_percent/people), 2)

print(
    f"Totol bill is : {bill_with_tip} and so each person should pay {total_tip} as tip")
