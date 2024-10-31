# spelling_bee.py

def pangram_bonus(word, puzzle_letters):
    """Returns 7 if every character in letters is in words.
    Otherwise it returns 0.
    """
    for c in puzzle_letters:
        if c not in word:
            return 0
    return 7

def word_score(word, required_letter, puzzle_letters):
    """Returns the score for word according to these rules:
    - Words with 3 or fewer letters score 0 points.
    - A 4-letter or more word scores 1 point per letter, e.g.
      'apple' scores 5.
    - A word that uses all seven puzzle letters is called
      a *pangram* and gets 7 extra points.
    """
    #
    # first check if the word is too short or doesn't contain the required
    # letter
    #
    if required_letter not in word or len(word) < 4:
        return 0
    
    #
    # check that all the letters in word are in letters
    #
    for c in word:
        if c not in puzzle_letters:
            return 0
    
    #
    # if we get here, the word is long enough and contains the required letter
    #
    return len(word) + pangram_bonus(word, puzzle_letters)

#
# Main code to solve a Spelling Bee Puzzle                                      

# sample
# letters = 'SIGLENP'
# required_letter = 'G'

# June 20, 2024
letters = 'LGXNCEI'
required_letter = 'I'

##letters = 'DIEMNTC'
##required_letter = 'C'

file_object = open('words.txt')
num_words = 0
total_score = 0
best_word = ''
best_word_score = 0
for w in file_object:
    w = w.strip().upper()
    score = word_score(w, required_letter, letters)
    total_score += score
    if score > 0:
        num_words += 1
        print(w, score)
        if score > best_word_score:
            best_word = w
            best_word_score = score
        

#file_object.close()

print()
print(f'     Number of words: {num_words}')
print(f'         Total score: {total_score}')
print()
print(f'Highest scoring word: {best_word}, {best_word_score} points')

