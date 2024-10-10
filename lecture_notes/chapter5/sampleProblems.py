# numQuestions.py

#
# Write a program that prints the hurricane category and whether it is a major
# hurricane for a given wind speed. See homework 5 for details.
#
# The [Saffir-Simpson hurricane
# scale](https://en.wikipedia.org/wiki/Saffir%E2%80%93Simpson_scale) ranks the
# severity of hurricanes based on their wind speed. The scale ranges from 1
# (least severe) to 5 (most severe):
#
# - Category 1 hurricane: wind speed 119 to less than 154 km/h
# - Category 2 hurricane: wind speed 154 to less than 178 km/h
# - Category 3 hurricane: wind speed 178 to less than 209 km/h
# - Category 4 hurricane: wind speed 209 to less than 252 km/h
# - Category 5 hurricane: wind speed 252 km/h or more
#
# A wind speed of less than 119 km/h is not considered a hurricane. Categories 3,
# 4, and 5 are considered "major" hurricanes.
#
def q1():
    wind_speed = float(input('Enter wind speed in km/h: '))
    category = -1

    if wind_speed < 119:
        category = 0
    elif 119 <= wind_speed < 154:
        category = 1
    elif 154 <= wind_speed < 178:
        category = 2
    elif 178 <= wind_speed < 209:
        category = 3
    elif 209 <= wind_speed < 252:
        category = 4
    else:
        category = 5

    # print results
    if category == 0:
        print('not a hurricane')
    else:
        print(f'Category {category} hurricane!')
        if category >= 3:
            print('This is a major storm!')

    



    

# q1()

#
# Write a program that prints all the numbers from 1 to 100 that are multiple
# of both 3 and 5, but not multiples of 7.
#
def q2():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0 and n % 7 != 0:
            print(n)


#
# Write a program that prints all the numbers from 100 to 999
# that are evenly divisible by the sum of its digits.
#
def q3():
    # 101
    count = 0
    for a in range(1, 10):
        # a == 1
        for b in range(0, 10):
            # b == 0
            for c in range(0, 10):
                # c == 1
                digit_sum = a + b + c  # 2
                n = 100*a + 10*b + c # 100*1 + 10*0 + 1 = 101
                if n % digit_sum == 0:
                    print(n)
                    count += 1
    print(f'{count} numbers')


















