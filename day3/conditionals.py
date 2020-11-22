height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("Enter your age: "))
    if age < 15:
        bill = 7
        print(f"Child tickets is: ${bill}")

    elif age <= 18:
        bill = 10
        print(f"Youth tickets is: ${bill}")
    else:
        bill = 15
        print(f"Adult tickets is: ${bill}")

    wants_photos = input("Wants photos? Y / N: ")

    if wants_photos == "Y":
        bill += 3
    print(f"Total bill is: ${bill}")
else:
    print("You cannot ride the rollercoaster")
