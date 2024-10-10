# numQuestions.py

def q1():
    wind_speed = float(input('Enter the wind speed in km/h: '))
    category = -1
    is_major = False

    if wind_speed < 119:
        category = 0
    elif 119 <= wind_speed < 154:
        category = 1
    elif 154 <= wind_speed < 178:
        category = 2
    elif 178 <= wind_speed < 209:
        category = 3
        is_major = True
    elif 209 <= wind_speed < 252:
        category = 4
        is_major = True
    else:  # 252 km/h or more
        category = 5
        is_major = True

    # print the results
    if category == 0:
        print(f'A wind speed of {wind_speed} km/h is not a hurricane.')
    else:
        print(f'A wind speed of {wind_speed} km/h is a Category {category} hurricane.')
        if is_major:
            print('It is a major hurricane.')
        else:
            print('It is not a major hurricane.')

# q1()

#
# Write a program that prints all the numbers from 1 to 1000 that are multiple
# of both 3 and 5, but not multiples of 7.
#
def q2():
    for i in range(1, 1001):
        if i % 3 == 0 and i % 5 == 0 and i % 7 != 0:
            print(i)

# q2()

#
# Write a program that prints all the numbers from 100 to 999 that are evenly
# divisible by the sum of its digits.
#
def q3():
    count = 0
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                num = a * 100 + b * 10 + c
                digit_sum = a + b + c
                if num % digit_sum == 0:
                    print(f'{num} = {digit_sum} * {num // digit_sum}')
                    count += 1
    print(f'There are {count} numbers that are evenly divisible by the sum of its digits.')

# q3()
