# print_long_lines.py

def chop(s):
    """Removes 1 trailing '\n' (if there is one).
    """
    if s == '':
        return s
    elif s[-1] == '\n':
        return s[:-1]
    else:
        return s

def compress_string(s, max_len):
    """Returns only the first max_len - 4 characters of s, and then ' ...'. 

    If the length of s is less than, or equal to, max_len, s is returned
    unchanged. The returend string will always have length less than, or equal
    to, max_len.

    >>> compress_string('put the oatmeal in the yellow bowl', 25)
    'put the oatmeal in th ...'
    >>> compress_string('William James McMahon', 20)
    'William James Mc ...'
    """
    if len(s) <= max_len:
        return s
    else:
        result = s[:max_len-4]
        result += ' ...'
        return result

def print_long_lines(filename, max_len):
    """Prints the lines in filename that are longer than max_len characters.
    """
    file = open(filename)
    line_number = 1
    num_long_lines = 0
    print(f'These are lines over {max_len} in "{filename}":')
    for line in file:
        # When reading a line from a file in this way, the line usually has a
        # '\n' character on the right end. '\n' is not counted when we talk
        # about the length of a line. So we remove one trailing '\n' with
        # chop.
        line = chop(line)
        n = len(line) # or to count tabs as 4 spaces: n = len(line) + 3*line.count('\t')
        if n > max_len:
            num_long_lines += 1
            short_line = compress_string(line, 30)
            print(f'     line {line_number:3} is length {n}: "{short_line}"')
        line_number += 1

    if num_long_lines == 0:
        print(f'     "{filename}" has no lines longer than {max_len}')

print_long_lines('test_long_lines.py', 120)
#print_long_lines('num_long_lines.py')
