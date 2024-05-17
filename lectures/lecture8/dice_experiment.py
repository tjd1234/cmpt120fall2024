# dice_experiment.py

#
# Question: If you roll 5 6-sided dice 1000 times, what's
# the chance that on at least one of those rolls all the
# dice have the same value?
#

import random

def roll_die():
  """ Randomly returns 1, 2, 3, 4, 5, or 6.
  """
  return random.randrange(1, 7)

def roll_once():
    """ Rolls 5 6-sided dice until all show the same value.
    Returns 1 if they are all the same, 0 otherwise.
    """
    d1 = roll_die()
    d2 = roll_die()
    d3 = roll_die()
    d4 = roll_die()
    d5 = roll_die()
    if d1 == d2 and d2 == d3 and d3 == d4 and d4 == d5:
        return 1
    else:
        return 0

def run_experiment(num_tries = 1000):
    print(f'Rolling 5 6-sided dice {num_tries} times ...')
    success = 0
    for trial in range(num_tries):
        success += roll_once()

    print(f'In {num_tries} throws, {success} time(s) they were all the same')
    pct = 100 * success / num_tries
    print(f'about {pct:.2f}% chance of rolling five dice all the same')

run_experiment(1000000)
