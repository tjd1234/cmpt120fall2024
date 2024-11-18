# count_letters.py

def count_letters(s):
    """Returns a dictionary with the frequency of each character in s.
    """
    letters = {}
    for c in s:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters

def test_count_letters():
    test_strings = ['title', 'Simon Fraser University', '']
    for s in test_strings:
        print(f'"{s}"\n   {count_letters(s)}')

# test_count_letters()

def dictionary_frequency():
    """Prints the frequency of each character in all the words in words.txt.
    """
    # read() returns the contents of the file as one big string
    big_string = open('words.txt', 'r').read().strip()
    print(count_letters(big_string))

# dictionary_frequency()

def dictionary_frequency_2():
    """Prints the frequency of each letter in words.txt from highest to lowest.
    """
    #
    # get the frequency dictionary for words.txt
    #
    big_string = open('words.txt', 'r').read().strip()
    freq = count_letters(big_string)
    freq.pop('\n')  # remove the newline character

    #
    # copy all the letter:count pairs into a list
    # as [count, letter] pairs
    #
    freq_list = []
    for letter in freq:
        pair = [freq[letter], letter]
        freq_list.append(pair)
    
    #
    # sort the list from highest to lowest count
    #
    freq_list.sort()
    freq_list.reverse()
    
    #
    # print the sorted list
    #
    for count, letter in freq_list:
        print(f'{letter}: {count}')
    
dictionary_frequency_2()