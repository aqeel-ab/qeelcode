def longestPalindrome(s:str) -> str:
    def expand(left:int, right:int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""

    for i in range(len(s)):
        
        odd = expand(i, i)       # Odd length palindromes
        even = expand(i, i + 1)  # Even length palindromes

        if len(odd) > len(longest):
            longest = odd

        if len(even) > len(longest):
            longest = even

    return longest

#Manual test cases
#print(longestPalindrome("babad"))  # bab or aba
#print(longestPalindrome("cbbd"))   # bb
#print(longestPalindrome("a"))      # a
#print(longestPalindrome("ac"))     # a or c
#print(longestPalindrome(""))       # empty string