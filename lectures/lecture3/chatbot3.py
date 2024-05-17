# chatbot3.py

#
# This chatbot choses a greeting at random. It uses lists and the
# random.choice function to do this.
#

#
# the random.choice function used below is in the random module, and so we
# must import here
#
import random

#
# a list of possible greetings (one will be chosen at random later)
#
greetings = ['Hello', 'Bonjour', 'Hola', 'Konnichiwa',
             'Guten tag', 'Asalaam alaikum'
            ]

# ask the user for some input
name = input("What's your name? ")

# print something based on the input
greeting = random.choice(greetings)
#print(greeting + ' ' + name + '!')
print(f'{greeting} {name}!')

# ask the user for some input
height = input('How tall are you? ')

# print something based on the input
print()
print(f"Wow, {height} is so tall!")
print("I'm just a program, so have neither width nor height.")
