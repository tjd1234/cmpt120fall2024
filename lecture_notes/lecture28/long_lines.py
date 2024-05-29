# long_lines.py

def chop(s):
    """Removes one '\n' from the right end of s, if there is one.
    """
    if s == '':
        return s
    elif s[-1] == '\n':
        return s[:-1]  # all but the last character
    else:
        return s

def compress_string(s, max_len):
    """Returns a string that is at most max_len characters long.
    If s is longer than max_len, then ' ...' is appended to the end.
    """
    if len(s) <= max_len:
        return s
    else:
        result = s[:max_len-4]
        result += ' ...'
        assert len(result) == max_len  # check that the result is the right length
        return result

def print_long_lines(filename, max_len):
    """Prints the lines in filename that are longer than max_len.

    Tab characters, '\t', count as a single character. In some editors they are
    expanded to, say, 4 spaces. This can cause some confusion when determining
    how long a line is since the length of a '\t' depends on the program used to
    view the line.
    """
    textfile = open(filename)
    line_num = 1
    long_line_count = 0
    print(f'In "{filename}", these lines are over {max_len} characters:')
    for line in textfile:
        # When reading from a file like this, the line usually comes with a
        # '\n' character at the end, which we don't want to count as part of
        # the line length. So we "chop" off the trailing '\n'.
        n = len(chop(line))
        if n > max_len:
            long_line_count += 1
            short_line = compress_string(line, min(20, max_len))
            print(f'     line {line_num:3}, {n} characters: "{short_line}"')
        line_num += 1

    if long_line_count == 0:
        print(f'     No lines with more than {max_len} characters!')


print_long_lines('test_long_lines.py', 100)
