# reverse_words_dict.py

import time

#
# print the program description
#
print('Finds all the words that are the reverse of another word.')
print('Uses a dictionary to store the words.\n')

#
# read all the words into a dictionary
#
print('Reading words from words.txt ...')
file_obj = open('words.txt', 'r')
word_dict = {}
for line in file_obj:
    word = line.strip()
    word_dict[word] = True

#
# count the number of words that are the reverse of another word
#
print('Counting the number of words that are the reverse of another word ...')
start_time = time.time()
rev_word_count = 0
for word in word_dict:
    rev = word[::-1]      # word[::-1] is the reverse of word
    if rev in word_dict:  # this line is fast because word_dict is a dictionary
        rev_word_count += 1
end_time = time.time()
elapsed_time = end_time - start_time

#
# print the results
#
print(f'\nNumber of words that are the reverse of another word: {rev_word_count}')
print(f'Time taken: {elapsed_time} seconds')
