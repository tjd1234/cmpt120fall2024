# random_products.py

import random

things = ['towel','coconut','light bulb','shoelace','shampoo',
          'potato','dog toy','hamster treat']
verbs = ['straightener','curler','dryer','densifier','stretcher',
         'de-linter']
mod1 = ['super','mini','mega','transparent','massive','neural']
mod2 = ['digital','analog','electric','solar-powered','auto-tuned']

n = input('How many product names do you want? ')
n = int(n)

print()
for i in range(n):
	thing = random.choice(things)
	verb = random.choice(verbs)
	m1 = random.choice(mod1)
	m2 = random.choice(mod2)

	name = m1 + ' ' + m2 + ' ' + thing + ' ' + verb
	print(f'{i+1}. {name}')
