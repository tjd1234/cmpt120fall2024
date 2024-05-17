# age_in_seconds.py

years = input('How many years old are you? ')
years = float(years)

seconds_in_hr = 60 * 60
seconds_in_day = 24 * seconds_in_hr
seconds_in_year = 365 * seconds_in_day

print("You're at least this many seconds old:", years * seconds_in_year)
