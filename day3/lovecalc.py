print("Welcome to the love calculator! ")
name1 = input("What is your name?: ")
name2 = input("What is your lovers name?: ")

names = name1 + name2
lower_case_names = names.lower()

t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
true = t+r+u+e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
love = l+o+v+e

love_score = int(str(true) + str(love))
# print(love_score)

if love_score > 90:
    print(f"Perfect match! Your love score is : {love_score}")
elif(love_score >= 40) and (love_score <= 50):
    print(f"Good match! Your love score is : {love_score}")
else:
    print(f"Your love score is : {love_score}")
