# chp8.py

def file_write_test():
    

def same1(s, t):
    """Returns True if s == t, False otherwise.
    Only uses ==, !=, etc. to compare single characters.
    Using a for loop.
    """
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if s[i] != t[i]:
            return False

    return True

def test_same1():
    print('testing same1 ...')
    assert same1('hello', 'hello') == True
    assert same1('hello', 'ello') == False
    assert same1('hello', 'Hello') == False
    assert same1('', '') == True
    assert same1('', 'a') == False
    print(' ...all same1 tests passed')

#test_same1()

def same2(s, t):
    """Returns True if s == t, False otherwise.
    Uses ==, !=, etc. to compare single characters.
    Using a while loop.
    """
    if len(s) != len(t):
        return False
    
    i = 0
    while i < len(s):
        if s[i] != t[i]:
            return False
        i += 1
        
    return True

def test_same2():
    print('testing same2 ...')
    assert same2('hello', 'hello') == True
    assert same2('hello', 'ello') == False
    assert same2('hello', 'Hello') == False
    assert same2('', '') == True
    assert same2('', 'a') == False
    print(' ...all same2 tests passed')

# test_same1()
test_same2()

######################################

def reverse1(s):
    """Returns a copy of s in reverse order.
    Using a for loop.
    """
    result = ''
    for c in s:
        result = c + result
    return result

def test_reverse1():
    print('testing reverse1 ...')
    assert reverse1('') == ''
    assert reverse1('a') == 'a'
    assert reverse1('ab') == 'ba'
    assert reverse1('abc') == 'cba'
    assert reverse1('hello, world!') == '!dlrow ,olleh'
    assert reverse1('racecar') == 'racecar'
    print(' ...all reverse1 tests passed')

test_reverse1()

def reverse2(s):
    """Returns a copy of s in reverse order.
    Using a while loop.
    """
    result = ''
    i = 0
    while i < len(s):
        result = s[i] + result
        i += 1
    return result

def test_reverse2():
    print('testing reverse2 ...')
    assert reverse2('') == ''
    assert reverse2('a') == 'a'
    assert reverse2('ab') == 'ba'
    assert reverse2('abc') == 'cba'
    assert reverse2('hello, world!') == '!dlrow ,olleh'
    assert reverse2('racecar') == 'racecar'
    print(' ...all reverse2 tests passed')

test_reverse2()

def is_palindrome(s):
    """Returns True if s is a palindrome (i.e. equal to its 
    reverse), False otherwise.
    """
    return s == s[::-1]
    #return same1(s, reverse1(s))

def test_is_palindrome():
    print('testing is_palindrome ...')
    assert is_palindrome('') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('aa') == True
    assert is_palindrome('aaa') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('hello, world!') == False
    print(' ...all is_palindrome tests passed')

# test_is_palindrome()
