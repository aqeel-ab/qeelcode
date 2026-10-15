
def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)

    reversed_num = 0

    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    reversed_num *= sign

    if reversed_num < -(2**31) or reversed_num > 2**31 - 1:
        return 0

    return reversed_num

# Manual tests
#print(reverse(123))          # Expected: 321
#print(reverse(-123))         # Expected: -321
#print(reverse(120))          # Expected: 21
#print(reverse(1534236469))   # Expected: 0
#print(reverse(0))            # Expected: 0