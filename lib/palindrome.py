import re
def longest_palindromic_substring(s: str):
    """
    Given a string s, return the longest palindromic substring.
    """

    punctuation_marks = '!?.";'
    #Earliest exit condition is an invalid argument type passed to the function
    if type(s) != str:
        raise ValueError("Invalid data type argument passed to the function. A string should be used.")
    
    s = s.lower()
    s = re.sub(r'[^\w\s]', '', s) # Removal of punctuatuon marks
    s = s.replace(" ", "")
    
    print(s)
    length_of_string = len(s)
    #String should be converted to lowercase and be stripped to avoid counting empty spaces

    # Handling cases that can have early exits
    if length_of_string == 1:
        return s
    
    if s == '':
        raise TypeError("Empty string provided.")
    
    n = len(s)
    if n < 2:
        return s
    
    start = 0
    max_len = 1

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_curr_len = max(len1, len2)
        if max_curr_len > max_len:
            max_len = max_curr_len
            start = i - (max_len - 1) // 2
            
    return s[start:start + max_len]

print(longest_palindromic_substring('A nut for a jar of tuna'))