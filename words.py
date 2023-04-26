def print_upper_words(lst):
    """
        >>> This will take an array and print out uppercase
    """
    for idx in lst:
        print(word.upper())

def print_upper_words(lst):
    """
        >>> This will take an array and print out if begins with e
    """
    for idx in lst:
        if idx.lower().startswith("e"):
            print(idx.upper())

def print_upper_words(lst, must_start_with):
    """
        >>> This will take an array and print out
    """
    for idx in lst:
        for char in must_start_with:
            if idx.startswith(char):
                print(idx.upper())
                break
