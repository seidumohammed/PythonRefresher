current_age = input("What is your current age: ")
current_age_as_int = int(current_age)
years_on_earth = 90
# years_remaining = years_on_earth - current_age_as_int
# months_remaining = years_remaining * 12
# weeks_remaining = years_remaining * 52
# days_remaining = years_remaining * 365

years_left_on_earth = years_on_earth - current_age_as_int
month_left_on_earth = (years_left_on_earth*12)
weeks_left_on_earth = (years_left_on_earth*52)
days_left_on_earth = (years_left_on_earth*365)

print(f"You have {years_left_on_earth} years,{month_left_on_earth} months,{weeks_left_on_earth} weeks,{days_left_on_earth} days on earth.")

# print("You have {years_remaining} years,{months_remaining} months, {weeks_remaining} weeks, and {days_remaining} days to live")
