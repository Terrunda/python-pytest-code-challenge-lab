from palindrome import longest_palindromic_substring
import pytest


# Handling normal cases

def test_with_string_argument_of_one_palindrome():
    """Test whether the function is able to determine the longest palindomric substring from a given argument that is valid."""
    normal_test = longest_palindromic_substring('cbbd')
    assert normal_test == 'bb'

def test_with_two_character_inputs():
    """
    This is a test that indiciates whether the function can recognize two characters within a string that can be considered a palindrome. 
    e.g: an example of 'ac' should return 'a' or 'c'
    """
    two_characters_test = longest_palindromic_substring('ac')
    assert two_characters_test == 'a, c'

def test_with_a_palindrome_string():
    """This is a test that checks whether a palindrome passed as an argument will return the same input."""
    palindrome_argument = 'racecar'
    palindrome_test = longest_palindromic_substring(palindrome_argument)
    assert palindrome_test == palindrome_argument

def test_with_two_possible_palindromes():
    """Test to determine the function's ability to detect 2 longest possible palindromic susbstring within a string of a length greater than 2 characters."""
    two_palindromes_test = longest_palindromic_substring('babad')
    assert two_palindromes_test == 'bab, aba'
    

# Handling edge cases.

def test_with_empty_string_input():
    """Test to determine how the function can handle an empty string argument passed to the function."""
    empty_string_test = longest_palindromic_substring('')
    assert empty_string_test == "No palindrome found."

def test_with_a_non_string_argument_passed_to_the_function():
    """Tests that the function will raise an error if the argument passed is not a string."""
    with pytest.raises(ValueError):
        longest_palindromic_substring(1234)

def test_with_single_string_input():
    """This will test that the function will return a single character as a single character is a valid palindrome."""
    single_character_test = longest_palindromic_substring('a')
    assert single_character_test == 'a'

def test_with_string_argument_with_no_palindrome():
    """Test to determine how the function handles a valid string argument that does not contain a palindrome."""
    no_palindrome_test = longest_palindromic_substring('qwdswk')
    assert no_palindrome_test ==  "No palindrome found."