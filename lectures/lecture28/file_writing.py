# files_writing.py

def write_example():
    # open a file for writing
    outfile = open('output.txt', 'w')  # 'w' means write

    # write some lines
    outfile.write('This is a line 1\n')
    outfile.write('This is a line 2\n')
    outfile.write('\n')
    outfile.write('The line above is blank\n')

write_example()
