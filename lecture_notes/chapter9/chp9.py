# chp9.py

#
# Open the list of words
#
file_obj = open('words.txt', 'r')

#
# Create a list of words
#
words_list = []
for line in file_obj:
    line = line.strip()  # remove \n from the end of line
    words_list.append(line)

print(f'... read in {len(words_list)}')

#
# Ask user to enter words.
#
#
# The expression "w in word_list" is used to check if w is in the list of words.
# It does this checking by scanning through the list one word at a time. If w is
# not in the list then it will check all the words in the list (more than
# 113,000!). This is not efficient ... but it works well enough this program,
# and you likely won't notice the delay. Later in the course we will learn about
# a far more efficient way to do this using dictionaries.
# 

while True:
    w = input('Word to check: ')
    w = w.strip()
    if w in words_list:
        print(f'{w} IS an English word')
    else:
        print(f'{w} is NOT an English word')
    print()
