# spellcheck_lecture.py

def read_words(fname):
    """Read a file of words, one per line, and return a dictionary of the
    words.

    The keys are the words, and the values are all 1. Whitespace characters at
    the beginning and end of each word are stripped off.

    Ignore duplicate words in the file.

    For example, suppose words.txt contained these 4 words:

        shoes
        hats
        glove
        shoes
        socks

    Then:

        >>> words = read_words('words.txt')
        >>> words
        {'shoes': 1, 'hats': 1, 'glove': 1, 'socks': 1}
    """
    all_words = {}
    word_file = open(fname)
    for w in word_file:
        w = w.strip()
        all_words[w] = 1
    return all_words


def get_misspelled(line, word_dict):
    """Returns a list of all the words in line that are misspelled.

    A word is considered misspelled if it has more than one character and also
    doesn't appear as a key in word_dict.

    If the same misspelled word appears more than once, then it only appears
    once in the returned list.

    >>> words = read_words('words.txt')
    >>> get_misspelled('I like a glove and socks', words)
    ['and', 'like']
    """
    # store the words in a dictionary to remove duplicates
    misspelled = {}
    for w in line.split():
        if len(w) > 1 and w not in word_dict:
            misspelled[w] = 1

    # convert the dictionary to a list
    unique_words = list(misspelled.keys())
    unique_words.sort()
    return unique_words















def clean_text(text):
    """Remove all non-letter characters from text.

    Keeps just alphabetic characters and spaces.

    >>> clean_text('Hello, world!')
    'Hello  world'
    """
    cleaned_text = ''
    for char in text:
        if char.isalpha() or char == ' ':
            cleaned_text += char # keep spaces and letters
        else:
            cleaned_text += ' '  # replace other characters with spaces
    return cleaned_text

def spellcheck_file(fname):
    """Print all the misspelled words in a file, including line number.
    """
    good_words = read_words('enable1.txt')
    textfile = open(fname)
    line_num = 1
    for line in textfile:
        line = clean_text(line)
        line = line.lower()
        misspelled = get_misspelled(line, good_words)
        if misspelled != []:
            # the join method combines all the strings onto a list,
            # using the string before the . as the seperator
            bad_words = ', '.join(misspelled)
            print(f'line {line_num}: {bad_words}')
        line_num += 1

spellcheck_file('dracula.txt')
