height = float(input("enter height in m: "))
weight = float(input("enter weight in kg: "))

bmi = round(weight / height ** 2)

if bmi <= 18.5:
    print(f"You're underweight, your bmi is: {bmi}")
elif bmi < 25:
    print(f"You have a normal weight, your bmi is: {bmi}")
elif bmi < 30:
    print(f"You're overwight, your bmi is: {bmi}")
elif bmi < 35:
    print(f"You're obese, your bmi is: {bmi}")
else:
    print(f"You're clinically obese, your bmi is: {bmi}")
