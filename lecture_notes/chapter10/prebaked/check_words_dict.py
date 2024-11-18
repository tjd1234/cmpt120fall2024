# check_words_dict.py

#
# Check if a word is in a list of English words. Stores the words in a Python
# dictionary.
#

#
#
# Open the list of words
#
file_obj = open('words.txt', 'r')

#
# Create a list of words
#
words_dict = {}
for line in file_obj:
    line = line.strip()  # remove \n from the end of line
    words_dict[line] = True

print(f'... read in {len(words_dict)}')

#
# Ask user to enter words.
#
#
# The expression "w in word_dict" is used to check if w is in the dictionary of
# words. It does this very efficiently: it does not scan through the list one
# word at a time. Instead, Python dictionaries are implemented using a clever
# trick called a hash table, and "in" with a dictionary can almost instantly
# tell you whether the word is in the dictionary or not.
# 

while True:
    w = input('Word to check: ')
    w = w.strip()
    if w in words_dict:
        print(f'{w} IS an English word')
    else:
        print(f'{w} is NOT an English word')
    print()
