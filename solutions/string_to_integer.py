
def myAtoi(s: str) -> int:
    i = 0
    n = len(s)

    # Step 1: Skip leading whitespace
    while i < n and s[i] == " ":
        i += 1

    # Step 2: Check for an optional sign
    sign = 1

    if i < n and s[i] == "-":
        sign = -1
        i += 1
    elif i < n and s[i] == "+":
        i += 1

    # Step 3: Read digits and build the number
    num = 0

    while i < n and s[i].isdigit():
        digit = int(s[i])
        num = num * 10 + digit
        i += 1

    # Step 4: Apply the sign
    num *= sign

    # Step 5: Clamp to the 32-bit signed integer range
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    if num < INT_MIN:
        return INT_MIN

    if num > INT_MAX:
        return INT_MAX

    return num


# Manual tests
#print(myAtoi("42"))                 # Expected: 42
#print(myAtoi(" -042"))              # Expected: -42
#print(myAtoi("1337c0d3"))           # Expected: 1337
#print(myAtoi("words and 987"))      # Expected: 0
#print(myAtoi("-91283472332"))       # Expected: -2147483648
#print(myAtoi("91283472332"))        # Expected: 2147483647
#print(myAtoi("+17"))                # Expected: 17
#print(myAtoi(""))                   # Expected: 0
