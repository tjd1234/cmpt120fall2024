# count_letters.py

def count_letters(s):
    """Returns a dictionary with the frequency of each character in s.
    """
    freq_dict = {}
    for c in s:
        if c in freq_dict:
            fre
    return freq_dict

def check_count_letters():
    test_strings = ['title', 'Simon Fraser University', '']
    for s in test_strings:
        print(f'"{s}"\n   {count_letters(s)}')

# check_count_letters()

# def dictionary_frequency():
#     """Prints the frequency of each character in all the words in words.txt.
#     """
#     pass

# dictionary_frequency()

# def dictionary_frequency_2():
#     """Prints the frequency of each letter in words.txt from highest to lowest.
#     """
#     pass

# dictionary_frequency_2()
