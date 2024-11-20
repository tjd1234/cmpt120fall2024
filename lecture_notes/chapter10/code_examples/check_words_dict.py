# check_words_dict.py

#
# Check if a word is in a list of English words. Stores the words in a Python
# dictionary.
#

# check_words_list.py

#
# Check if a word is in a list of English words. Stores the words in a Python
# list.
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

while True:
    w = input('Word to check: ')
    w = w.strip()
    if w in words_dict:
        print(f'{w} IS an English word')
    else:
        print(f'{w} is NOT an English word')
    print()
