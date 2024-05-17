# bus1.py

"""
- Children 12 and under ride *free*.
- Youths 13 to 18, or seniors 65 and older, pay *concession* fares.
- Everyone else pays *full* fares.
"""

age = input('How old are you? ')
age = int(age)

if age < 0:
    print(f"{age} is not a valid age!")
elif age <= 12:
    print('Child: free')
elif age <= 18:
    print('Youth: concession fare')
elif age >= 65:
    print('Senior: concession fare')
else:
    print('Adult: full fare')
