from anagram import is_anagram


def main():
    # Testing the anagram challenge:
    assert is_anagram('abcdefg', 'gefabcd') == True  # True anagram
    assert is_anagram('foo', 'bar') == False  # Not an anagram
    assert is_anagram('the_same', 'the_same') == False  # Not truly an anagram


if __name__ == '__main__':
    main()
