# colatz.py

def collatz_step(n):
    if n % 2 == 0:       # is n even?
        return n // 2
    else:                # is n odd?
        return 3 * n + 1

def collatz(n):
    """Repeatedly applies collatz_step to n until it reaches 1.
    Fact: No one knows if there is some positive integer value for n
    that causes this function to loop forever.
    """
    original_n = n
    step_count = 0
    while n > 1:
        print(n)
        n = collatz_step(n)
        step_count += 1
    #print(n)
    print(f'{step_count} steps to reduce {original_n} to 1')

collatz(10)
