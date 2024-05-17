# group_maker.py

#
# This programs helps divide a group into smaller groups. Given the total_num
# number of people and group size, it reports how many groups are needed, and
# how many people are leftover.
#
# For example:
#
#    How many people are there? 106
#    What size are the groups? 9
#
#    Make this many groups: 11
#    This many people will be leftover: 7
#

num_people = input('How many people are there? ')
num_people = int(num_people)

group_size = input('What size are the groups? ')
group_size = int(group_size)

num_groups = num_people // group_size   # // is integer division
leftover = num_people % group_size

print()
print("Make this many groups:", num_groups)
print("This many people will be leftover:", leftover)
