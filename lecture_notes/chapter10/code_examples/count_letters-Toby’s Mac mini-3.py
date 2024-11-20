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
    freq_dict.pop('\n')
    print(freq_dict)

# dictionary_frequency()

{'a': 68574, 'h': 20186, 'e': 106752, 'd': 34548, 'i': 77392, 'n': 60505, 'g': 27832, 's': 86526, 'l': 47003, 'r': 64963, 'v': 9186, 'k': 9366, 'w': 8533, 'o': 54538, 'f': 12706, 'b': 17794, 'c': 34281, 'u': 31151, 't': 57029, 'm': 24739, 'p': 25789, 'y': 13473, 'x': 2700, 'j': 1780, 'z': 3750, 'q': 1632}

# def dictionary_frequency_2():
#     """Prints the frequency of each letter in words.txt from highest to lowest.
#     """
#     pass

# dictionary_frequency_2()
