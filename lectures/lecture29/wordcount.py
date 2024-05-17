# wordcount.py

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


def count_words(fname):
    """Count the number of words in a file.
    """
    # word_count is an initially empty dictionary that stores the count of each
    # word
    word_count = {}

    contents = open(fname)
    for line in contents:
        # split the line into words
        words = clean_text(line).split(' ')

        # add all the words to the dictionary
        for w in words:
            w = w.strip()   # remove whitespace at the beginning and end
            if w != '':     # ignore empty strings
                if w in word_count:
                    word_count[w] += 1
                else:
                    word_count[w] = 1

    return word_count


def print_top10(fname):
    """Prints the top 10 most frequent words in fname.

    >>> print_top10('dracula.txt')
    the 7205
    and 5589
    I 4831
    to 4371
    of 3572
    a 2880
    in 2384
    that 2375
    he 1931
    was 1866
    """
    word_count = count_words(fname)

    # make a list if [count, word] pairs
    count_pairs = []
    for w in word_count:
        pair = [word_count[w], w]
        count_pairs.append(pair)

    # sort the words from highest count to lowest
    #
    # when sorting a list, Python's built-in sort compares the first element of
    # the list first
    count_pairs.sort()
    count_pairs.reverse()  # reverse the list, we want highest count to lowest

    # print the top 10 words
    for pair in count_pairs[:10]:
        print(pair[1], pair[0])

