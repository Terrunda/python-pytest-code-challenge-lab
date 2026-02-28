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
    assert two_characters_test == 'a'

def test_with_a_palindrome_string():
    """This is a test that checks whether a palindrome passed as an argument will return the same input."""
    palindrome_argument = 'racecar'
    palindrome_test = longest_palindromic_substring(palindrome_argument)
    assert palindrome_test == palindrome_argument

def test_with_two_possible_palindromes():
    """Test to determine the function's ability to detect 2 longest possible palindromic susbstring within a string of a length greater than 2 characters."""
    two_palindromes_test = longest_palindromic_substring('babad')
    assert two_palindromes_test == 'bab'
    
def test_with_integers_as_strings_for_a_palindrome():
    """Tests to determine the functions'a ability to determine a palindrome of a string data type consisting of numbers only"""
    assert longest_palindromic_substring("1412449583141") == '141'

# Handling edge cases.
def test_with_empty_string_input():
    """Test to determine how the function can handle an empty string argument passed to the function."""
    with pytest.raises(TypeError):
        longest_palindromic_substring('')

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
    assert no_palindrome_test ==  "q"

def test_with_string_argument_containing_white_spaces():
    """Test whether the function can find a palindrome when an argument contains a string with white-spaces"""
    white_spaces_test = longest_palindromic_substring('A nut for a jar of tuna')
    assert white_spaces_test == 'anutforajaroftuna'
    pass

def test_with_string_containing_capital_letters():
    """Test whether the function can find a palindrome when a string argument is passed containing one or more passengers."""
    capital_letters_test = longest_palindromic_substring('tEnaNt')
    assert capital_letters_test == 'nan'