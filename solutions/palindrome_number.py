
def isPalindrome(x: int) -> bool:
    # Negative numbers cannot be palindromes.
    if x < 0:
        return False

    original = x
    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    return original == reversed_num


# Manual tests
#print(isPalindrome(121))    # Expected: True
#print(isPalindrome(-121))   # Expected: False
#print(isPalindrome(10))     # Expected: False
#print(isPalindrome(0))      # Expected: True
#print(isPalindrome(1221))   # Expected: True
#print(isPalindrome(123))    # Expected: False
