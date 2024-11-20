# reverse_words_list.py

import time

#
# print the program description
#
print('Finds all the words that are the reverse of another word.')
print('Uses a list to store the words.\n')

#
# read all the words into a list
#
print('Reading words from words.txt ...')
word_list = open('words.txt', 'r').read().split('\n')
word_list.remove('')  # remove the empty string caused b the end of the file

#
# count the number of words that are the reverse of another word
#
print('Counting the number of words that are the reverse of another word ...')
start_time = time.time()
rev_word_count = 0
for word in word_list:
    rev = word[::-1]      # word[::-1] is the reverse of word
    if rev in word_list:  # this line is slow because it scans through the list
        rev_word_count += 1
end_time = time.time()
elapsed_time = end_time - start_time

#
# print the results
#
print(f'\nNumber of words that are the reverse of another word: {rev_word_count}')
print(f'Time taken: {elapsed_time} seconds')
