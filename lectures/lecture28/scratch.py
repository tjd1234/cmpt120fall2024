# scratch.py

#import os
#print(os.getcwd())
#print(os.listdir(os.getcwd()))

def chop(s):
    """Removes one '\n' from the right end of s, if there is one.
    """
    if s == '':
        return s
    elif s[-1] == '\n':
        return s[:-1]  # all but the last character
    else:
        return s

def get_all_lines(fname):
    textfile = open(fname)
    all_lines = []
    for line in textfile:
        all_lines.append(line)
    return all_lines

entire_file = open('joke.txt').read()
print(entire_file)
