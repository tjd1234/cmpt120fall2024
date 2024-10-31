# word_example.py

for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(f'Letter {letter.upper()}')
    file_object = open('words.txt')
    line_num = 0
    for w in file_object:
        w = w.strip()
        if w.count(letter) >= 3:
            line_num += 1
            print(f'   {line_num}. {w}')


##file_object = open('words.txt')
##line_num = 0
##for w in file_object:
##    w = w.strip()
##    if 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w and 'y' in w:
##        line_num += 1
##        print(f'{line_num}. {w}')
