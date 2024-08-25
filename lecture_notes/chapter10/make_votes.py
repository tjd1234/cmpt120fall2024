# make_votes.py

import random

names = 'Ned Sally JoJo Cindy Euchariah Augustus Lou Betty Drew Martha'.split()
print(names)

n = 10000
fname = 'votes_out.txt'
print(f'Writing {n} random votes to {fname} ...')
out = open(fname, 'w')
for i in range(n):
    out.write(f'{random.choice(names)}\n')
out.close()
print('Done.')