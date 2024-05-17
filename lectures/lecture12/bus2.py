# bus2.py

"""
- Children 12 and under ride *free*.
- Youths 13 to 18, or seniors 65 and older, pay *concession* fares.
- Everyone else pays *full* fares.
"""

age = input('How old are you? ')
age = int(age)

if age < 0:
    print(f"{age} is not a valid age!")
elif 0 <= age <= 12:
    print('Child: free')
elif 12 < age <= 18:
    print('Youth: concession fare')
elif 65 <= age:
    print('Senior: concession fare')
else:
    print('Adult: full fare')
