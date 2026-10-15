
def isMatch(s: str, p: str) -> bool:
    m = len(s)
    n = len(p)

    # dp[i][j] means the first i characters of s
    # match the first j characters of p.
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Empty string matches an empty pattern.
    dp[0][0] = True

    # Handle patterns such as a*, a*b*, and a*b*c*.
    for j in range(2, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            elif p[j - 1] == "*":
                # Treat the preceding element as zero occurrences.
                dp[i][j] = dp[i][j - 2]

                # Or use one or more occurrences if they match.
                if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]


# Manual tests
#print(isMatch("aa", "a"))             # Expected: False
#print(isMatch("aa", "a*"))            # Expected: True
#print(isMatch("ab", ".*"))            # Expected: True
#print(isMatch("aab", "c*a*b"))        # Expected: True
#print(isMatch("mississippi", "mis*is*p*."))  # Expected: False
#print(isMatch("", "a*"))              # Expected: True
