# Lecture 28 Notes

Reading and writing files is a common Python task. There are two main kinds of
files: **text files**, that consist of plain text and can viewed and edited in
an editor like Mu. And **binary files**, which are every other kind of file,
e.g. image files, video files, specially formatted files for particular
applications, and so on.

While there are many ways to process files, in these notes we only discuss
reading text files line-by-line.

## Determining What Folder You're In

Before we get into reading files, here's a useful trick for being sure what
folder or directory (*folder* and *directory* mean the same thing) you're
reading from:

```
>>> import os

>>> os.getcwd()
'C:\\Users\\james\\Documents\\courses\\cmpt120fall2022'

>>> os.listdir(os.getcwd())
['a1.py', 'a2.py', 'lectures']
```

`os.getcwd()` returns the *current working directory*, i.e. the directory that
Python will read files from by default. This tells you where Python will
read/write files by default.

`os.listdir(os.getcwd())` returns a list of all the files and folders in the
current working directory.


## Reading a Text File Line by Line

[joke.txt](joke.txt) is a text file containing this:

```
Who’s there?
A broken pencil.
A broken pencil who?
Never mind. It’s pointless.
```

This code reads it line-by-line:

```python
textfile = open('joke.txt')     # assumes joke.txt is in the same folder
for line in textfile:           # as the file this program is in
    print(line)
```

It prints this:

```
Who's there?

A broken pencil.

A broken pencil who?

Never mind. It's pointless.

```

The print-out is *double-spaced* because each line of `joke.txt` ends with a
`\n` (which causes a new line when printed), and Python's `print` always adds a
`\n` after what it prints. If we want single-spacing, we can tell `print` *not*
add a final `\n`:

```python
textfile = open('joke.txt')
for line in textfile:
    print(line, end='')     # don't put a \n after line
```

Or we can check which lines end with a `\n` and not print the final `\n`:

```python
textfile = open('joke.txt')
for line in textfile:
    if line[-1] == '\n':
        print(line[:-1])    # don't print the last character of line
    else:
        print(line)
```

Removing a single `\n` from the end of a string is a common enough operation
that it is useful to write a function to do it:

```python
def chop(s):
    """If s ends with a \n, remove it. Otherwise returns s unchanged.
    """
    if s == '': 
        return ''
    elif s[-1] == '\n': 
        return s[:-1]
    else:
        return s
```

Now the previous program can be written more simply:

```python
textfile = open('joke.txt')
for line in textfile:
    print(chop(line))
```

It prints this:

```
Who's there?
A broken pencil.
A broken pencil who?
Never mind. It's pointless.
```

## Reading Lines of Text File into a List

Something that's often useful to do is to read the lines of file into a list:

```python
textfile = open('joke.txt')
all_lines = []
for line in textfile:
    all_lines.append(chop(line))  # chop removes a \n at the end line,
                                  # if there is one
print(all_lines)
print()
print(f'number of lines: {len(all_lines)}')
```

This prints:

```
["Who's there?", 'A broken pencil.', 'A broken pencil who?', "Never
mind. It's pointless."]

number of lines: 4
```

This is useful enough to put into its own function:

```python
def get_line_list(fname):
    textfile = open(fname)
    all_lines = []
    for line in textfile:
        all_lines.append(chop(line))
    return all_lines
```

Now we can write code like this:

```python
all_lines = get_line_list('joke.txt')
print(all_lines)
print()
print(f'number of lines: {len(all_lines)}')
```

Which prints:

```
["Who's there?", 'A broken pencil.', 'A broken pencil who?', 
"Never mind. It's pointless."]

number of lines: 4
```

Having all the lines in a list makes some operations easy. For example, this
prints the original file:

```python
all_lines = get_line_list('joke.txt')
for line in all_lines:
    print(line)
```

Output:

```
Who's there?
A broken pencil.
A broken pencil who?
Never mind. It's pointless.
```

This prints the file in reverse order by line:

```python
all_lines = get_line_list('joke.txt')
all_lines.reverse()
for line in all_lines:
    print(line)
```

Output:

```
Never mind. It's pointless.
A broken pencil who?
A broken pencil.
Who's there?
```

This prints the file with line numbers:

```python
all_lines = get_line_list('joke.txt')
line_num = 1
for line in all_lines:
    print(f'{line_num:3} {line}')
    line_num += 1
```

Output:

```
  1 Who's there?
  2 A broken pencil.
  3 A broken pencil who?
  4 Never mind. It's pointless.
```

You can also do simple (and slow!) text searching. For example, this prints all
the lines that contain the string `'pencil'`:

```python
all_lines = get_line_list('joke.txt')
for line in all_lines:
    if 'pencil' in line:
        print(line)
```

Output:

```
A broken pencil.
A broken pencil who?
```

### The Built-in `readlines` Function

Python has a built-in method called `readlines` that will reads a test file into
a list of strings:

```
>>> f = open('changelog.txt')
>>> all_lines = f.readlines()
>>> len(all_lines)
714
```

In practice, this is probably what you should use. We have written our own
versions above to understand how they work and learn more about Python.


## Challenge: Checking if Any Lines in a File are Too Long

Write a program that takes the name of a text file as input, and prints just the
lines in the file that are *longer* than 100 characters.

Print the line number at the start of the line so that the user knows where to
look for it in the file.

If the file has no lines over 100 characters, then print a helpful message like
'No lines with more than 100 characters!'.

**Sample solution** See [long_lines.py](long_lines.py).
[test_long_lines.py](test_long_lines.py) is the file it uses for testing.


## Writing to a Text File

Basic writing to a text file is straightforward. For example
([file_writing.py](file_writing.py)):

```python
# open a file for writing
outfile = open('output.txt', 'w')    # 'w' means write

# write some lines
outfile.write('This is a line 1\n')  # \n is needed to end the line
outfile.write('This is a line 2\n')
outfile.write('\n')
outfile.write('The line above is blank\n')

outfile.close()
```

**Careful!** If `output.txt` already exists, this will be overwrite it, i.e.
delete the previous contents. If it doesn't exist, then it will be created.

Here is are the contents of `output.txt` after running the code:

```
This is a line 1
This is a line 2

The line above is blank
```

## Reading a Web Page

Finally, Python provides an easy way to read the contents of a web page as
string. For example:

```python
import urllib.request

def get_web_page_text(url):
    """ Retrieve the contents of a web page.
    """
    socket = urllib.request.urlopen(url)
    return socket.read()

page = get_web_page_text('https://www.sfu.ca/')
print(page)
```

This returns the web page *as one big string*, which may be quite unreadable! 
If you want to create your own
[web scraper](https://en.wikipedia.org/wiki/Web_scraping) or web browser, then 
this is a good start.
