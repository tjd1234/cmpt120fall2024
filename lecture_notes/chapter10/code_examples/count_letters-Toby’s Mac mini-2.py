# count_letters.py

def count_letters(s):
    """Returns a dictionary with the frequency of each character in s.
    """
    freq_dict = {}
    for c in s:
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1
    return freq_dict

def check_count_letters():
    test_strings = ['title', 'Simon Fraser University', '']
    for s in test_strings:
        print(f'"{s}"\n   {count_letters(s)}')

# check_count_letters()

def dictionary_frequency():
    """Prints the frequency of each character in all the words in words.txt.
    """
    all_words = open('words.txt', 'r').read()
    freq_dict = count_letters(all_words)
    freq_list.p
    print(freq_dict)

dictionary_frequency()

# def dictionary_frequency_2():
#     """Prints the frequency of each letter in words.txt from highest to lowest.
#     """
#     pass

# dictionary_frequency_2()
